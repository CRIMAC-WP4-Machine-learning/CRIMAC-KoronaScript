import sys
import KoronaScript as ks
import KoronaScript.Modules as ksm

"""
This example applies pulse compression and stores
the results as an netcdf.
"""

ksi = ks.KoronaScript()
ksi.add(ksm.NetcdfWriter(Active="true",
                         DirName=sys.argv[1],
                         MainFrequency="38",
                         WriterType="CHANNEL_GROUPS",
                         GriddedOutputType="PULSE_COMPRESSION",
                         WriteAngels="true",
                         FftWindowSize="2",
                         DeltaFrequency="1",
                         ChannelGroupOutputType="PULSE_COMPRESSION"))

ksi.run(src=sys.argv[1], dst=sys.argv[2])
