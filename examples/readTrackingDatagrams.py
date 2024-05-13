import datetime
import os
import sys
import pandas as pd
import xml.etree.ElementTree as ET

from util.rawindex import index
from util.simrad_parsers import SimradConfigParser, SimradTrackInfoParser, SimradTrackBorderParser, SimradTrackContentsParser, SimradXMLParser
from util.date_conversion import dt64_to_nt, UTC_NT_EPOCH

# Read track datagrams example

# After running the Korona tracking module, this script can be run on the rawfiles to extract the tracking information
# and save it as a csv-file.

# The script is run from the command line with two arguments:
# 1. The directory containing the raw files
# 2. The directory where the output csv-files are saved
# 3. (Optional) The path to the work file. If work file is specified, the track files are updated based on the work file

# Example: python readTrackingDatagrams.py /PATH/TO/Korona/rawfiles /PATH/TO/save_path /PATH/TO/work.work

# The output csv file column headers should correspond the proposed SONAR-netCDF standard for single targets

def update_track_files(work_dict, track_info, track_borders):
    # select only valid ids
    track_info = track_info[track_info.valid == 1]

    # Remove replaced ids based on work file
    for replaced_id in work_dict['extra']['trackEdits']['replacedIds']:
        assert replaced_id in track_info.id.values

        track_info = track_info[track_info.id != replaced_id]

    # Remove invalid and replaced ids in track_border dict
    track_borders = track_borders[track_borders['id'].isin(track_info.id.unique())]
    track_borders = track_borders.reset_index(drop=True)

    # Add changed tracks from workfile
    idx = len(track_borders.index)
    for track in work_dict['extra']['trackEdits']['tracks']['track']:
        datagram_type = "TBR0"
        id = track['id']
        channel = track['channel']

        for ping in track['ping']:
            nttime_low, nttime_high = dt64_to_nt(np.datetime64(ping['ntDate']))
            data = [datagram_type, nttime_low, nttime_high, id, channel, ping['minDepth'], ping['maxDepth'],
                    ping['peakDepth'], ping['ntDate']]
            track_borders.loc[idx] = data
            idx += 1

    # TODO update track info as well
    return track_info, track_borders

def read_work(work_file_path):
    """ Function to read work file (xml) and return a list of dictionaries """
    # Read xml file
    tree = ET.parse(work_file_path)

    # Get a dictionary based on xml file contents
    root = tree.getroot()
    work_dict = {}
    for i, child in enumerate(root):
        work_dict[child.tag] = child.attrib
        parse_child(child, work_dict[child.tag])

    work_dict = clean_work_dict(work_dict)
    return work_dict

def nt_to_datetime(nt_time):
    """ Function to convert NT time to datetime
        NT time is 100 ns intervals since 1601-01-01 """
    # convert from 100 ns intervals to microseconds, 100 ns interval = 0.1 microseconds
    return UTC_NT_EPOCH + datetime.timedelta(microseconds=nt_time / 10)

def clean_work_dict(work_dict):
    for key, val in work_dict.items():
        if key == 'ntDate':
            work_dict[key] = nt_to_datetime(convert_str(val)).strftime('%Y-%m-%d %H:%M:%S.%f')
        else:
            if type(val) is dict:
                clean_work_dict(val)
            elif type(val) is list:
                for i, item in enumerate(val):
                    if type(item) is dict:
                        clean_work_dict(item)
                    elif type(item) is str:
                        work_dict[key][i] = convert_str(item)
            elif type(val) is str:
                work_dict[key] = convert_str(val)
    return work_dict

def convert_str(item):
    """ Function to convert string to int or float if possible """
    try:
        if '.' in item:
            return np.float64(item)
        else:
            return np.int64(item)
    except:
        return item

def parse_child(child, child_dict):
    """ Function to parse child of root """
    for i, grandchild in enumerate(child):
        if len(grandchild) > 0:
            if grandchild.tag in child_dict:
                # print("Warning: tag already exists", grandchild.tag)
                prev_content = child_dict[grandchild.tag]
                child_dict[grandchild.tag] = [prev_content]
                child_dict[grandchild.tag].append(grandchild.attrib)
                parse_child(grandchild, child_dict[grandchild.tag][-1])
            else:
                child_dict[grandchild.tag] = grandchild.attrib
                parse_child(grandchild, child_dict[grandchild.tag])
        else:
            if grandchild.tag not in child_dict:
                child_dict[grandchild.tag] = []

            if len(grandchild.attrib) > 0:
                child_dict[grandchild.tag].append(grandchild.attrib)
            else:
                if grandchild.text is not None:
                    text = grandchild.text.split()
                    child_dict[grandchild.tag] = text
    return child.attrib, child.tag


def parse_datagram(msg, length, typ):
    '''
    Parse a datagram according to the format dictionary.
    '''
    if typ == 'TBR0':
        parser = SimradTrackBorderParser()
        return parser._unpack_contents(msg, length)
    elif typ == 'TNF0':
        parser = SimradTrackInfoParser()
        return parser._unpack_contents(msg, length)
    elif typ == 'TTC0':
        parser = SimradTrackContentsParser()
        return parser._unpack_contents(msg, length)
    elif typ == "CON0":
        # Head datagram, needed to get frequencies
        parser = SimradConfigParser()
        return parser._unpack_contents(msg, length)
    elif typ == "XML0":
        parser = SimradXMLParser()
        return parser._unpack_contents(msg, length, 0)
    else:
        raise ValueError(f"Unknown datagram type: {typ}")


if __name__ == "__main__":
    import numpy as np

    # Get input parameters
    par = {"koronadir": sys.argv[1],  # Directory with Korona raw files
           "save_path": sys.argv[2]}  # Path where output csv-file is saved

    if len(sys.argv) == 4:
        par['work_path'] = sys.argv[3]  # Path to work file

    # Get raw files
    relevant_datagrams = []
    raw_files = [os.path.join(par['koronadir'], f) for f in os.listdir(par['koronadir']) if f.endswith('.raw')]

    # Loop through raw files
    transducer_frequencies = []
    for raw_file in raw_files:
        for pos, typ, length, msg in index(raw_file):
            if len(transducer_frequencies) == 0 and typ == "XML0":
                parsed_datagram = parse_datagram(msg, length, typ)
                for freq in parsed_datagram['configuration']:
                    transducer_frequencies.append(float(parsed_datagram['configuration'][freq]['transducer_frequency']))
                transducer_frequencies = np.array(sorted(transducer_frequencies))

            # If datagram type is relevant, parse it
            if typ in ['TBR0', 'TNF0', 'TTC0']:
                parsed_datagram = parse_datagram(msg, length, typ)
                relevant_datagrams.append(parsed_datagram)

        # Retrieve tracking border datagrams and save in csv file
        tracking_border = [datagram for datagram in relevant_datagrams if datagram['type'] == 'TBR0']
        df_tracking_border = pd.DataFrame(tracking_border)
        # df_tracking_border.to_csv(os.path.join(par['outputdir'], f'{raw_file.replace(".raw", "")}_TBR0.csv'))

        # Retrieve tracking info datagrams and save in csv file
        tracking_info = [datagram for datagram in relevant_datagrams if datagram['type'] == 'TNF0']
        df_tracking_info = pd.DataFrame(tracking_info)
        # df_tracking_info.to_csv(os.path.join(par['outputdir'], f'{raw_file.replace(".raw", "")}_TFN0.csv'))

    # Update track files based on work file, if work file is specified
    if "work_path" in par:
        work_dict = read_work(par['work_path'])
        df_tracking_info, df_tracking_border = update_track_files(work_dict, df_tracking_info, df_tracking_border)

        # Ensure timestamp is in datetime format, not string
        df_tracking_border['timestamp'] = pd.to_datetime(df_tracking_border['timestamp'])

    # Remove targets that are not valid according to tracking info datagrams
    df_tracking_border = df_tracking_border[df_tracking_border['id'].isin(df_tracking_border.id.unique())]
    df_tracking_border = df_tracking_border.reset_index(drop=True)

    # convert to standard name format
    df_tracking_border = df_tracking_border.rename(columns={'id': 'single_target_identifier',
                                                            'timestamp': 'ping_time',
                                                            'channel': 'frequency_index',
                                                            'minDepth': 'single_target_start_range',
                                                            'maxDepth': 'single_target_stop_range',
                                                            'peakDepth': 'single_target_range',
                                                            })
    # Add the frequency index
    df_tracking_border['frequency'] = transducer_frequencies[df_tracking_border['frequency_index'].values - 1]  # Count starts from 1 (?)

    # Add the number of targets in each ping
    df_tracking_border['single_target_count'] = df_tracking_border.groupby(["ping_time"])['ping_time'].transform('size')

    # Format ping time as string object
    df_tracking_border['ping_time'] = df_tracking_border['ping_time'].apply(lambda x: x.strftime("%Y-%m-%dT%H:%M:%S.%fZ"))

    # Drop columns that are not used in the standard
    df_tracking_border = df_tracking_border.drop(columns=['nttime_low', 'nttime_high', 'type', 'frequency_index'])

    # Save
    df_tracking_border.to_csv(par['save_path'], index=False)
