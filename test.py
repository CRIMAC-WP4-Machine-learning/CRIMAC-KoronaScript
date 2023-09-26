from KoronaScript import *

ks = KoronaScript(Categorization='categorization.xml',
                  HorizontalTransducerOffsets='HorizontalTransducerOffsets.xml')

ks.add(Tracking())
ks.add(EmptyPingRemoval())
ks.add(Comment(LineBreak='false', Label='CW_0256ms'))
ks.add(TemporaryComputationsBegin(Active='passive'))
ks.add(ChannelRemoval(Channels=[1,5,9,13,17],KeepSpecified='true'))
ks.add(Writer(RelativeDirectory='CW_0256ms'))
ks.add(TemporaryComputationsEnd())

ks.write()
