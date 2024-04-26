import sys
import KoronaScript as ks
import KoronaScript.Modules as ksm

ks = ks.KoronaScript(TransducerRanges='examples/TransducerRanges.xml')

ks.add(ksm.Tracking())
ks.add(ksm.EmptyPingRemoval())
ks.add(ksm.Comment(LineBreak='false', Label='CW_0256ms'))
ks.add(ksm.TemporaryComputationsBegin())
ks.add(ksm.ChannelRemoval(Channels=[1,5,9,13,17],KeepSpecified='true'))
ks.add(ksm.Writer(RelativeDirectory='CW_0256ms', DirectoryName='cr_out'))
ks.add(ksm.TemporaryComputationsEnd())

if len(sys.argv) == 1:
    print(f'Usage: {sys.argv[0]} <input> <output dir>')
    print(f'(or: "{sys.argv[0]} --config" to print configuration)')
elif sys.argv[1] == '--config':
    ks.write()
else:
    ks.run(src=sys.argv[1], dst=sys.argv[2])
