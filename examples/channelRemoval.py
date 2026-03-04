import sys
import KoronaScript as ks
import KoronaScript.Modules as ksm

ksi = ks.KoronaScript(TransducerRanges='examples/TransducerRanges.xml')

ksi.add(ksm.Tracking())
ksi.add(ksm.EmptyPingRemoval())
ksi.add(ksm.Comment(LineBreak='false', Label='CW_0256ms'))
ksi.add(ksm.TemporaryComputationsBegin())
ksi.add(ksm.ChannelRemoval(Channels=[1, 5, 9, 13, 17], KeepSpecified='true'))
ksi.add(ksm.Writer(RelativeDirectory='CW_0256ms', DirectoryName='cr_out'))
ksi.add(ksm.TemporaryComputationsEnd())

if __name__ == '__main__':
    ksi.run(src=sys.argv[1], dst=sys.argv[2])
