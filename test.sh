#!/bin/bash

set -e

# Run a set of tests using internal IMR data sets

export PYTHONPATH=.

export TESTSET=~/src/data/testset
# This is the messor data example (for FM2PC?):
#    /data/crimac/2021/T2021002/ACOUSTIC/EK80/EK80_RAWDATA/
# Not sure what this is
#    /data/crimac/2023/T2023001/ACOUSTIC/EK80/EK80_RAWDATA/

if ! test -e "$TESTSET"; then
   echo "Test set not found: $TESTSET"
   exit -1
fi

echo "Running: channelRemoval"
mkdir -p test_cr.out
python3 examples/channelRemoval.py $TESTSET test_cr.out

echo "Running: tsDetection"
mkdir -p test_tsdet.out
python3 examples/tsDetection.py $TESTSET test_tsdet.out

echo "Running: pulseCompression"
mkdir -p test_pc.out
python3 examples/pulseCompression.py $TESTSET test_pc.out

# Too complicated to set up
# python3 examples/processFMtestdata.py
