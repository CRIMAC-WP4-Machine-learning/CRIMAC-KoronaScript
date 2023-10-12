# Run examples on styx.hi.no

This a recipe is how to run KoronaScript on styx on the FM test data. This should also work on other servers that have access to the ´/data/´ folders.

# Install LSSS
## Licence
You need an LSSS licence file. Create ~/marec/license and add the licence file in that directory.

`cd ~`

`mkdir marec`

`cd marec`

`mkdir license`

Copy the file into the folder (this works if you have scp locally)

`scp marec-license-Nils-Olav-Handegard-Institute-of-Marine-Research-Norway.lic nilsolav@styx.hi.no:/home/nilsolav/marec/license`

## Donwload and install LSSS
Required steps:

`cd ~`

`mkdir lsss`

`cd lsss`

`wget https://marec.no/tmp/lsss-2.16.0-alpha-20230922-1417-linux.zip`

`unzip lsss-2.16.0-alpha-20230922-1417-linux.zip`

`rm lsss-2.16.0-alpha-20230922-1417-linux.zip`

You first need to tell linux where to find korona Set the env variable (this can also be set in your shell init, e.g. .zshrc).:

`export LSSS=~/lsss/lsss-2.16.0-alpha/korona`

# Prepare python

## Use venv to install packages

Create and activate a virtual environment:

`cd ~`

`mkdir venv` (I prefer to have the venv in a separate folder)

`cd venv`

Create a virtual environment called korona. You can choose you own name.

`python3 -m venv korona`

After creating the enviroment you need to activate it:

`source ~/venv/korona/bin/activate`

Important: Remember to activate the environment every time you are starting a new session.

## Install python packages
Use pip install after activating your venv

`pip install xarray`

`pip install matplotlib`

`pip install pandas`

And any other packages that you may find useful.

Use ´pip list´ to see which ones are installed in you venv.

## Clone the CRIMAC-Korona-Script package

`cd ~`

`mkdir repos` (I prefer to have the repositories in a separate directory)

`cd repos`

`git clone https://github.com/CRIMAC-WP4-Machine-learning/CRIMAC-KoronaScript`

Python also need to find the packages. Use the PYTHONPATH to do this (use colon to separate the paths):

`export PYTHONPATH=~/repos/CRIMAC-KoronaScript:$PYTHONPATH`

# Testing

Run a test script to see if everything is working. 

Create a temp directory to store results (can be set to anything you like):
`cd ~`

`mkdir tmp`

`cd ~/repos/CRIMAC-KoronaScript`

Make sure that the venv is activated and run 

`python ./examples/testFMtoPC_hi.py`

