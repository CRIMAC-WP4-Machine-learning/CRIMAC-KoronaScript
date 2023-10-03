from KoronaScript import *
import os
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np

"""

This example reads the T2023001 test set, applied pulse compression and store 
the results as an netcdf. the netcdf file is read and the pulse compressed data are plotted.

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

# Add the pulsecompression module and write to nc
ks.add(NetcdfWriter(Active = "true",
                    DirName = dirname,
                    MainFrequency = "38",
                    WriterType = "CHANNEL_GROUPS",
                    GriddedOutputType = "PULSE_COMPRESSION",
                    WriteAngels = "true",
                    FftWindowSize = "2",
                    DeltaFrequency = "1",
                    ChannelGroupOutputType = "PULSE_COMPRESSION"))
ks.write()
ks.run(src=inputdir, dst=outputdir)

# Read and plot processed nc files
dat  = xr.open_mfdataset(outputdir+dirname+'/*.nc', parallel = "True")


# There is no pc field in the data set?
dat_sub  = dat.sv['frequency'  == 38000].transpose()
quadmesh  = plt.pcolormesh(10*np.log10(dat_sub))
plt.show()
