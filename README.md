# Running Korona through Python

## Prerequisites

### Install LSSS/Korona.

This version of the KoronaScript is tested against lsss-2.16.0-alpha
version. LSSS and korona is usually placed at
`~/lsss/lsss-2.16.0-alpha` or a similar directory.

### Add license 

You need an LSSS licence. The licence have to be added according to the LSSS manual. the licence files are typically placed at the `~/marec/license` directory.

### Set system variables

This can be set at run time either by setting the LSSS environment
variable in the shell
~~~
export LSSS=~/lsss-2.16.0-alpha/korona
~~~
before running your script, or by adding
~~~
lsss = '~/lsss-2.16.0-alpha/korona'
os.environ["LSSS"] = lsss
~~~
to your script.

# Examples

## Convert raw data to pulse compressed data and store as net cdf file
See the ´examples/pusleCompression.py´ file.

## Convert old work files to new ones


