import KoronaScript.Modules as ksm
import KoronaScript as ks
import os
'''
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import sys
from netCDF4 import Dataset
import glob
import json
import pandas as pd
'''

# This is the messor data example
inputdir = '/data/crimac/2021/T2021002/ACOUSTIC/EK80/EK80_RAWDATA/'

# Write to temp directory
outputdir = '.' # '/home/nilsolav/tmp/'

# Filter the FM test data:
ksi = ks.KoronaScript(TransducerRanges = "/home/nilsolav/repos/CRIMAC-KoronaScript/examples/TransducerRanges.xml")

# Add the pulsecompression module and write to nc

ksi.add(ksm.Tracking(Active = "true",
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

ksi.write()
ksi.run(src=inputdir, dst=outputdir)
