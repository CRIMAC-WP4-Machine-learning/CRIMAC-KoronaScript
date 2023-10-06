# Running Korona through Python

## Prerequisites

### Install LSSS/Korona.

This version of the KoronaScript is tested against lsss-2.16.0-alpha
version. LSSS and korona is usually placed at
`~/lsss/lsss-2.16.0-alpha` or a similar directory.

Download the appropriate version from here:

https://marec.no/tmp/lsss-2.16.0-alpha-20230922-1417-linux.zip

https://marec.no/tmp/lsss-2.16.0-alpha-20230922-1417-windows.zip


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

# Updating

The modules are auto-generated from the JSON definitions found in
configuration using the script [util/genmodule.py](util/genmodule.py).

# Testing

You can run the [test.sh](test.sh) script to run each example on test data, and
you can use [compare.sh](compare.sh) to compare the original raw files to the
korona-generated ones (specify the two directories as command line
parameters).

# Example scripts

## Convert raw data to pulse compressed data and store as net cdf file
See the [examples/pulseCompression.py](examples/pulseCompression.py) file.

## Convert old work files to new ones

## Channel removal
