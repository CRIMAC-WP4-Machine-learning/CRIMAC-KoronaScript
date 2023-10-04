from KoronaScript import *
import os
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np

"""

This example reads the T2023001 test set, applies pulse compression and peak 
detection. The detected single targets are plotted on top of the pulse comresse data.

"""


# Set lsss env variable
lsss = '/home/nilsolav/lsss/lsss-2.16.0-alpha/'
os.environ["LSSS"] = lsss

# Input
inputdir = '/mnt/c/DATA/crimac/2023/T2023001/ACOUSTIC/EK80/EK80_RAWDATA/'
outputdir = '/mnt/c/DATAscratch/crimac-scratch/2023/T2023001/ACOUSTIC/GRIDDED/'
dirname = 'pc'

# Instanitate the class
ks = KoronaScript()

# Apply pc, sed and read the results.

# Test how well the algorithm is working on our test sets

# Check senstitivy to the parameters, are the results reliable?
