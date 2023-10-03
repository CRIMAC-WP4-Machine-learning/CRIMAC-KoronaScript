from KoronaScript import *
import sys

ks = KoronaScript(Categorization='categorization.xml',
                  HorizontalTransducerOffsets='HorizontalTransducerOffsets.xml')

ks.add(Tracking())
ks.add(EmptyPingRemoval())
ks.add(Comment(LineBreak='false', Label='CW_0256ms'))
ks.add(TemporaryComputationsBegin(Active='passive'))
ks.add(ChannelRemoval(Channels=[1,5,9,13,17],KeepSpecified='true'))
ks.add(Writer(RelativeDirectory='CW_0256ms'))
ks.add(TemporaryComputationsEnd())

if len(sys.argv)==1:
    # print config if no arguments are specified
    ks.write()
else:
    ks.run(src=sys.argv[1], dst=sys.argv[2])
