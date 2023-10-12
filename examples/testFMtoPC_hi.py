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

ksi.add(ksm.TsDetection(Active = "true",
                        DetectorType = "PEAK",
                        MinTS = "-66",
                        PulseLengthDeterminationLevel = "6",
                        MinEchoLength = "0.01",
                        MaxEchoLength = "1.8",
                        MaxGainCompensation = "6",
                        DoPhaseDeviationCheck = "true",
                        MaxPhaseDevSteps = "8",
                        MaxDepth = "40"))

ksi.write()
ksi.run(src = inputdir, dst = outputdir)
