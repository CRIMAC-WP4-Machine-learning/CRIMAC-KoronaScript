# Running Korona through Python

## Prerequisites

### Install LSSS/Korona.
This version of the KoronaScript is tested against lsss-2.16.0-alpha version. LSSS and korona is usually placed at `~/lsss/lsss-2.16.0-alpha` directory.

### Add license 
You need a LSSS licence. The licence have to be added according to the LSSS manual. the licence files are typically placed at the `~/marec/license` directory.

### Set system variables
this can be set at run time by adding 
~~~
lsss = '~/lsss-2.16.0-alpha/korona'
os.environ["LSSS"] = lsss
~~~
to your script, or by setting the env variable when starting the shell.

# Examples

## Convert raw data to pulse compressed data and store as net cdf file
See the ´example_pc.py´ file.

## Convert old work files to new ones


