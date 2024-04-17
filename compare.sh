#!/bin/bash

orig_dir=$1
output_dir=$2

export PYTHONPATH=.

for raw in $orig_dir/*.raw; do
    new=$output_dir/$(basename $raw .raw)-korona.raw
    echo
    echo Original: $raw
    echo Processed: $new
    echo
    python3 util/rawindex.py $raw > /tmp/tmp1
    python3 util/rawindex.py $new > /tmp/tmp2
    echo Datagram counts:
    echo Original:
    cut -f1 /tmp/tmp1 | sort | uniq -c
    echo Processed:
    cut -f1 /tmp/tmp2 | sort | uniq -c
    echo Diffs:
    diff /tmp/tmp1 /tmp/tmp2 | head -30
done
