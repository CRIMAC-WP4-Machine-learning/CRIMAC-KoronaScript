import sys
import KoronaScript as ks
import KoronaScript.Modules as ksm

ks = ks.KoronaScript(Categorization='categorization.xml',
                     HorizontalTransducerOffsets=
                     'HorizontalTransducerOffsets.xml')

ks.add(ksm.Tracking())
ks.add(ksm.EmptyPingRemoval())
ks.add(ksm.Comment(LineBreak='false', Label='CW_0256ms'))
ks.add(ksm.TemporaryComputationsBegin(Active='passive'))
ks.add(ksm.ChannelRemoval(Channels=[1,5,9,13,17],KeepSpecified='true'))
ks.add(ksm.Writer(RelativeDirectory='CW_0256ms'))
ks.add(ksm.TemporaryComputationsEnd())

if len(sys.argv) == 1:
    # print config if no arguments are specified
    ks.write()
else:
    ks.run(src=sys.argv[1], dst=sys.argv[2])
