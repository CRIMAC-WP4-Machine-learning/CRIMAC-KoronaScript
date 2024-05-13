import KoronaScript.Modules as ksm
import KoronaScript as ks
import os
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import sys
from netCDF4 import Dataset
import glob
import json
import pandas as pd

"""

This example reads the test data sets, applies pulse compression and plots and stores 
the results as an netcdf in the crimac scratch folder.

You need to store these parameters locally in a json file called processFMtestdata.json:
{
    "lsss" : "/home/nilsolav/lsss/lsss-2.16.0-alpha/",
    "DataSets" : "/home/nilsolav/repos/CRIMAC-data-organisation/DataSets.csv",
    "inputdir" : "/mnt/c/DATA/crimac/",
    "outputdir" : "/mnt/c/DATAscratch/"
}

"""

# Get input parameters
if os.path.exists('./examples/processFMtestdata.json'):
    with open('./examples/processFMtestdata.json', 'r') as f:
        par = json.load(f)
else:
    sys.exit('Parameter file is missing. Please add a json file. See comments in the script.')

if os.path.exists(par['DataSets']):
    with open(par['DataSets'], 'r') as f:
        DataSets = pd.read_csv(f)
else:
    sys.exit('DataSets.csv is missing in the given location. Clone the CRIMAC-data-organisation repository and edit the json file to point to the DataSets.csv file.')

# Set lsss env variable
os.environ["LSSS"] = par['lsss']
dirname = 'pc'


# Filter the FM test data:

ind_pulsetype = DataSets["pulsetype"] == 'FM'
ind_testset = [str(_dataset)[0] == "T" for _dataset in
               list(DataSets["dataset"])]
ind = ind_testset & ind_pulsetype
FMtestDataSets = DataSets[ind]

FMtestDataSets.to_csv('FMtestdata.csv')

for _testdata in FMtestDataSets["dataset"]:
    _FMtestDataSets = FMtestDataSets[FMtestDataSets["dataset"] == _testdata]
    inputdir = par["inputdir"] + _FMtestDataSets["RAW_files"].astype('string').values[0]
    outputdir = (par["outputdir"] + '/' + _FMtestDataSets[
        "start_time"] + '/' + _FMtestDataSets[
            "dataset"] + '/ACOUSTIC/GRIDDED/').astype('string').values[0]
    os.makedirs(outputdir, exist_ok=True)

    try:
        # Instanitate the class
        ksi = ks.KoronaScript()

        # Hack:
        if _testdata == 'T2023002':
            MainFrequency = "200"
        else:
            MainFrequency = "38"

        # Add the pulsecompression module and write to nc
        ksi.add(ksm.NetcdfWriter(Active="true",
                                 DirName=dirname,
                                 MainFrequency=MainFrequency,
                                 WriterType="CHANNEL_GROUPS",
                                 GriddedOutputType="PULSE_COMPRESSION",
                                 WriteAngels="true",
                                 FftWindowSize="2",
                                 DeltaFrequency="1",
                                 ChannelGroupOutputType="PULSE_COMPRESSION"))
        ksi.write()
        ksi.run(src=inputdir, dst=outputdir)  # Begrening på kjernar

        # List NC files
        ncfiles = glob.glob(outputdir + dirname + '/*.nc')

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
            y_pc_n = np.sqrt(np.square(data[i].pulse_compressed_re.mean(
                dim='sector')) + np.square(data[i].pulse_compressed_im.mean(dim='sector'))).transpose()
            # Plot the absolute values of the pc data
        quadmesh = ax[i].pcolormesh(10 * np.log10(y_pc_n))

        plt.savefig((par["outputdir"] + '/' + _FMtestDataSets["dataset"] + '.png').astype('string').values[0])
    except:
        print('**********************************************')
        print('Failed: ' + _testdata)
        print('**********************************************')
