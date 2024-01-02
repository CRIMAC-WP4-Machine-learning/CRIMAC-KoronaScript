import os
import sys
import pandas as pd

from util.rawindex import index
from util.simrad_parsers import SimradTrackInfoParser, SimradTrackBorderParser, SimradTrackContentsParser


# Read track datagrams example

# After running the Korona tracking module, this script can be run on the rawfiles to extract the tracking information
# and save it as a csv-file.

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
    else:
        raise ValueError(f"Unknown datagram type: {typ}")


if __name__ == "__main__":
    # Get input parameters
    par = {"koronadir": sys.argv[1],  # Directory with Korona raw files
           "outputdir": sys.argv[2]}  # Directory where output csv-files are saved

    # Get raw files
    relevant_datagrams = []
    raw_files = [os.path.join(par['koronadir'], f) for f in os.listdir(par['koronadir']) if f.endswith('.raw')]

    # Loop through raw files
    for raw_file in raw_files:
        for pos, typ, length, msg in index(raw_file):
            # If datagram type is relevant, parse it
            if typ in ['TBR0', 'TNF0', 'TTC0']:
                parsed_datagram = parse_datagram(msg, length, typ)
                relevant_datagrams.append(parsed_datagram)

        # Retrieve tracking border datagrams and save in csv file
        tracking_border = [datagram for datagram in relevant_datagrams if datagram['type'] == 'TBR0']
        df_tracking_border = pd.DataFrame(tracking_border)
        df_tracking_border.to_csv(os.path.join(par['outputdir'], f'{raw_file.replace(".raw", "")}_TBR0.csv'))

        # Retrieve tracking info datagrams and save in csv file
        tracking_info = [datagram for datagram in relevant_datagrams if datagram['type'] == 'TNF0']
        df_tracking_info = pd.DataFrame(tracking_info)
        df_tracking_info.to_csv(os.path.join(par['outputdir'], f'{raw_file.replace(".raw", "")}_TFN0.csv'))

        # TODO read TTCO datagrams