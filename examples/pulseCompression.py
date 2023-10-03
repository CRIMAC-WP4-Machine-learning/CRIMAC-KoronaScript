from KoronaScript import *
import os
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import sys

"""

This example reads the specified test set (e.g. T2023001), applies pulse compression and stores 
the results as an netcdf. the NetCDF file is read and the pulse compressed data are plotted.

"""

# Set lsss env variable
# lsss = '/home/nilsolav/lsss/lsss-2.16.0-alpha/'
# os.environ["LSSS"] = lsss

# Input
if len(sys.argv) != 3:
    print(f'Usage: {sys.argv[0]} inputdir outputdir')
    exit(0)
else:
    inputdir = sys.argv[1]
    outputdir = sys.argv[2]

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
dat  = xr.open_mfdataset(outputdir+'/'+dirname+'/*.nc', decode_times=False) # parallel = "True"


# There is no pc field in the data set?
dat_sub  = dat.sv['frequency'  == 38000].transpose()
quadmesh  = plt.pcolormesh(10*np.log10(dat_sub))
plt.show()
