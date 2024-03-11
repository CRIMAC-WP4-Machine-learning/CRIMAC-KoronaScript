import datetime
import os
import sys
import pandas as pd

from util.rawindex import index
from util.simrad_parsers import SimradConfigParser, SimradTrackInfoParser, SimradTrackBorderParser, SimradTrackContentsParser, SimradXMLParser

# Read track datagrams example

# After running the Korona tracking module, this script can be run on the rawfiles to extract the tracking information
# and save it as a csv-file.

# The script is run from the command line with two arguments:
# 1. The directory containing the raw files
# 2. The directory where the output csv-files are saved

# Example: python readTrackingDatagrams.py /PATH/TO/Korona/rawfiles /PATH/TO/save_path

# The output csv file column headers should correspond the proposed SONAR-netCDF standard for single targets

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
        #df_tracking_border.to_csv(os.path.join(par['outputdir'], f'{raw_file.replace(".raw", "")}_TBR0.csv'))

        # Retrieve tracking info datagrams and save in csv file
        tracking_info = [datagram for datagram in relevant_datagrams if datagram['type'] == 'TNF0']
        df_tracking_info = pd.DataFrame(tracking_info)
        #df_tracking_info.to_csv(os.path.join(par['outputdir'], f'{raw_file.replace(".raw", "")}_TFN0.csv'))

    # Remove targets that are not valid according to tracking info datagrams
    df_tracking_border = df_tracking_border[df_tracking_border['id'].isin(df_tracking_border.id.unique())]
    df_tracking_border = df_tracking_border.reset_index(drop=True)

    # convert to standard name format
    df_tracking_border = df_tracking_border.rename(columns={'id': 'single_target_identifier', 'timestamp': 'ping_time', 'channel': 'frequency_index',
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

    # Drop nt high and low columns
    df_tracking_border = df_tracking_border.drop(columns=['nttime_low', 'nttime_high', 'type', 'frequency_index'])

    # Save
    df_tracking_border.to_csv(par['save_path'], index=False)