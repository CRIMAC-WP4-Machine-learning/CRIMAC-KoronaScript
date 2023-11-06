from KoronaScript import *
from KoronaScript.Modules import *
import os
import json

import sys
import pandas as pd

from util.rawindex import index
from util.simrad_parsers import SimradTrackInfoParser, SimradTrackBorderParser, SimradTrackContentsParser

# Tracking example

# Below is the korona steps for tracking on individual frequencies

# The data we need to get out is the calibrated pulse compressed samples
# that belongs to each track and then calculate the TS(f)
# Set lsss env variable

# Create a local file named tracking.json containing
# '''
# {
#     "lsss" : "/home/nilsolav/lsss/lsss-2.16.0-alpha/",
#     "inputdir" : "/mnt/c/DATA/crimac/2023/T2023001/ACOUSTIC/EK80/EK80_RAWDATA/",
#     "outputdir" : "/mnt/c/DATAscratch/korona/",
#     "trranges" : "/home/nilsolav/repos/CRIMAC-KoronaScript/examples/TransducerRanges.xml"
# }
# '''
# Or call the scripts with parameters "inputdir" "outputdir" "lsss" "trranges"

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
    if os.path.exists('examples/tracking.json'):
        with open('examples/tracking.json','r') as f:
            par = json.load(f)
    elif len(sys.argv) != 5:
        print(f'Usage: {sys.argv[0]} inputdir outputdir lsss trranges')
        exit(0)
    else:
        par = {"inputdir": sys.argv[1],
               "outputdir": sys.argv[2],
               "lsss": sys.argv[3],
               "trranges": sys.argv[4]}

    os.environ["LSSS"] = par['lsss']

    # Set the path to the transducer ranges
    ks = KoronaScript(TransducerRanges = par['trranges'])

    '''
    ks.add(Comment(Active = "true",
                   LineBreak = "false",
                   Label = "Tracking setup",
                   Comment = ""))
    '''

    ks.add(EmptyPingRemoval(Active = "true"))

    '''
    ks.add(DataReduction(Active = "true",
                         BlindZone = "false",
                         MinRange = "14",
                         MinDepth = "",
                         TransducerRange = "false",
                         MaxRange = "26",
                         MaxDepth = ""))
    '''

    ks.add(Tracking(Active = "true",
                    TrackerType = "SED",
                    kHz = "38",
                    PlatformMotionType = "Floating",
                    MinTS = "-50",
                    PulseLengthDeterminationLevel = "5",
                    MinEchoLength = "0.005",
                    MaxEchoLength = "0.15",
                    MaxGainCompensation = "9",
                    DoPhaseDeviationCheck = "false",
                    MaxPhaseDevSteps = "10",
                    MaxTS = "-10",
                    MaxDepth = "27",
                    MaxAlongshipAngle = "5",
                    MaxAthwartshipAngle = "5",
                    InitiationGateFunction = {
                        "Alpha": 2.8,
                        "Beta": 2.8,
                        "Range": 0.1,
                        "TS": 20},
                    InitiationMinLength = "1",
                    GateFunction = {
                        "Alpha": 2.8,
                        "Beta": 2.8,
                        "Range": 0.1,
                        "TS": 20},
                    AlphaBetaEstimator = {
                        "Alpha": 0.9,
                        "Beta": 0.1},
                    MaxMissingPings = "4",
                    MaxMissingSamples = "2",
                    MaxMissingPingsFraction = "0.7",
                    MinTrackLength = "10",
                    MinSampleToLengthFraction = "1"))

    # run korona
    ks.write()
    ks.run(src=par['inputdir'], dst=par['outputdir']) # Begrening på kjernar

    # Read data and save in csv format together with the raw data
    relevant_datagrams = []
    raw_files = [os.path.join(par['outputdir'], f) for f in os.listdir(par['outputdir']) if f.endswith('.raw')]
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

        # TODO save tracking contents in csv format

    # Plot results
