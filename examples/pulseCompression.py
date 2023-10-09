from KoronaScript import *
from KoronaScript.Modules import *
import os
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import sys
from netCDF4 import Dataset
import glob

"""

This example reads the specified test set (e.g. T2023001), applies pulse compression and stores 
the results as an netcdf. the NetCDF file is read and the pulse compressed data are plotted.

"""

# Get input parameters
if os.path.exists('./examples/pulseCompression.json'):
    with open('./examples/pulseCompression.json', 'r') as f:
        par = json.load(f)
elif len(sys.argv) != 4:
    print(f'Usage: {sys.argv[0]} inputdir outputdir lsss ')
    exit(0)
else:
    par = {"inputdir": sys.argv[1],
           "outputdir": sys.argv[2],
           "lsss": sys.argv[3]}

# Set lsss env variable
os.environ["LSSS"] = par['lsss']

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
ks.run(src=par["inputdir"], dst=par["outputdir"]) # Begrening på kjernar

# List NC files
ncfiles = glob.glob(par["outputdir"]+'/'+dirname+'/*.nc')

# Open dataset for file 0
nc_dataset = Dataset(ncfiles[0], "r")
grp = list(nc_dataset.groups.keys())
data = [xr.open_dataset(ncfiles[0], group=_grp) for _grp in grp if not
        _grp == 'Environment']
data[0]
# Average across channels and calculate the absolute value from the complex pc
# values (Eq. 8 in
# https://github.com/CRIMAC-WP4-Machine-learning/CRIMAC-Raw-To-Svf-TSf/blob/main/Paper/Manuscript.pdf)

f, ax = plt.subplots(1, len(data))
for i in range(0, len(data)):
    y_pc_n = np.sqrt(np.square(data[i].pulse_compressed_re.mean(dim='sector')) +
                     np.square(data[i].pulse_compressed_im.mean(dim='sector'))).transpose()
    # Plot the absolute values of the pc data
    quadmesh  = ax[i].pcolormesh(10*np.log10(y_pc_n))
    
plt.show()

