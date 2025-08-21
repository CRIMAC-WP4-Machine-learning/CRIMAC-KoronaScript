#!/bin/bash

set -e

# Run a set of tests using internal IMR data sets

export PYTHONPATH=.
export TESTSET=/data/crimac/2023/T2023001/ACOUSTIC/EK80/EK80_RAWDATA/
# This is the messor data example (for FM2PC?):
#    /data/crimac/2021/T2021002/ACOUSTIC/EK80/EK80_RAWDATA/

if ! test -e "$TESTSET"; then
   echo "Testset not found: $TESTSET"
   exit -1
fi

mkdir -p test_cr.out
python3 examples/channelRemoval.py $TESTSET test_cr.out

mkdir -p test_fm2pc.out
python3 examples/testFMtoPC_hi.py $TESTSET test_fm2pc.out

# mkdir -p test_pc.out
# python3 examples/pulseCompression.py $TESTSET test_pc.out $LSSS
# Fails

# Too complicated to set up
# python3 examples/processFMtestdata.py
