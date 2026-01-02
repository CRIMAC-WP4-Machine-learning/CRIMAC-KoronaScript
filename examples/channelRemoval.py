import sys
import KoronaScript as ks
import KoronaScript.Modules as ksm

ks = ks.KoronaScript(TransducerRanges='examples/TransducerRanges.xml')

ks.add(ksm.Tracking())
ks.add(ksm.EmptyPingRemoval())
ks.add(ksm.Comment(LineBreak='false', Label='CW_0256ms'))
ks.add(ksm.TemporaryComputationsBegin())
ks.add(ksm.ChannelRemoval(Channels=[1, 5, 9, 13, 17], KeepSpecified='true'))
ks.add(ksm.Writer(RelativeDirectory='CW_0256ms', DirectoryName='cr_out'))
ks.add(ksm.TemporaryComputationsEnd())

ks.run(src=sys.argv[1], dst=sys.argv[2])
