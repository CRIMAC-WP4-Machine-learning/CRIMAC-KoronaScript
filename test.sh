#!/bin/bash

# Run a set of tests

export PYTHONPATH=.
export LSSS=lsss-2.15.0-alpha

mkdir -p test_pc.out

python3 examples/pulseCompression.py /data/crimac/2023/T2023001/ACOUSTIC/EK80/EK80_RAWDATA/ test_pc.out $LSSS
