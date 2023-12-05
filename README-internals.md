# Internals

## Updating

The modules are auto-generated from the JSON definitions found in
configuration using the script [util/genmodule.py](util/genmodule.py).

## Testing

You can run the [test.sh](test.sh) script to run each example on test data, and
you can use [compare.sh](compare.sh) to compare the original raw files to the
korona-generated ones (specify the two directories as command line
parameters).

## Example scripts

### Convert raw data to pulse compressed data and store as net cdf file
See the [examples/pulseCompression.py](examples/pulseCompression.py) file.

### Convert old work files to new ones

### Channel removal
See the [examples/channelRemoval.py](examples/channelRemoval.py) file.

### Single echo detection
See the [examples/singleEchoDetection.py](examples/singleEchoDetection.py) file.

### Tracking
See the [examples/tracking.py](examples/tracking.py) file.
