from KoronaScript import *

# Tracking example

# Below is the korona steps for tracking on individual frequencies

# The data we need to get out is the calibrated pulse compressed samples
# that belongs to each track and then calculate the TS(f)
# Set lsss env variable

lsss = '/home/nilsolav/lsss/lsss-2.16.0-alpha/'
os.environ["LSSS"] = lsss
inputdir = '/mnt/c/DATA/crimac/2023/T2023001/ACOUSTIC/EK80/EK80_RAWDATA/'
outputdir = '/mnt/c/DATAscratch/korona/'
'''
# Input
if len(sys.argv) != 3:
    print(f'Usage: {sys.argv[0]} inputdir outputdir')
    exit(0)
else:
    inputdir = sys.argv[1]
    outputdir = sys.argv[2]
'''


# Instanitate the class
ks = KoronaScript()

ks.add(Comment(Active = "true",
               LineBreak = "false",
               Label = "Tracking setup",
               Comment = ""))

ks.add(EmptyPingRemoval(Active = "true"))

ks.add(DataReduction(Active = "true",
                     BlindZone = "false",
                     MinRange = "14",
                     MinDepth = "",
                     TransducerRange = "false",
                     MaxRange = "26",
                     MaxDepth = ""))

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
ks.run(src=inputdir, dst=outputdir) # Begrening på kjernar

# Plot results
