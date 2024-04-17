import os
import json
import sys
import KoronaScript.Modules as ksm
from KoronaScript import KoronaScript

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


if __name__ == "__main__":
    # Get input parameters
    if os.path.exists('examples/tracking.json'):
        with open('examples/tracking.json', 'r') as f:
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
    ks = KoronaScript(TransducerRanges=par['trranges'])

    '''
    ks.add(Comment(Active = "true",
                   LineBreak = "false",
                   Label = "Tracking setup",
                   Comment = ""))
    '''
    # For T2023002
    # ks.add(ksm.ChannelRemoval(Channels=[2, 6, 10, 14, 18], KeepSpecified='true'))
    ks.add(ksm.EmptyPingRemoval(Active="true"))

    '''
    ks.add(DataReduction(Active = "true",
                         BlindZone = "false",
                         MinRange = "14",
                         MinDepth = "",
                         TransducerRange = "false",
                         MaxRange = "26",
                         MaxDepth = ""))
    '''

    ks.add(ksm.Tracking(Active="true",
                        TrackerType="SED",
                        kHz="38",
                        PlatformMotionType="Floating",
                        MinTS="-50",
                        PulseLengthDeterminationLevel="5",
                        MinEchoLength="0.005",
                        MaxEchoLength="0.15",
                        MaxGainCompensation="9",
                        DoPhaseDeviationCheck="false",
                        MaxPhaseDevSteps="10",
                        MaxTS="-10",
                        MaxDepth="27",
                        MaxAlongshipAngle="5",
                        MaxAthwartshipAngle="5",
                        InitiationGateFunction={
                            "Alpha": 2.8,
                            "Beta": 2.8,
                            "Range": 0.1,
                            "TS": 20},
                        InitiationMinLength="1",
                        GateFunction={
                            "Alpha": 2.8,
                            "Beta": 2.8,
                            "Range": 0.1,
                            "TS": 20},
                        AlphaBetaEstimator={
                            "Alpha": 0.9,
                            "Beta": 0.1},
                        MaxMissingPings="4",
                        MaxMissingSamples="2",
                        MaxMissingPingsFraction="0.7",
                        MinTrackLength="10",
                        MinSampleToLengthFraction="1"))

    # run korona
    ks.write()
    ks.run(src=par['inputdir'], dst=par['outputdir'])  # Begrening på kjernar
