# Running Korona through Python

## Prerequisites

KoronaScript depends on LSSS and Korona version 3.0.0.  The `LSSS`
environment variable can be set to point to an existing installation,
otherwise, the LSSS distribution will be automatically downloaded from
the Marec web pages and installed as part of this package.

# Usage

Import the modules:

	import KoronaScript as ks
	import KoronaScript.Modules as ksm

Create a script object:

	ks = ks.KoronaScript(Categorization='categorization.xml',
                     HorizontalTransducerOffsets='HorizontalTransducerOffsets.xml')

Add some modules:

	ks.add(ksm.EmptyPingRemoval())
	ks.add(ksm.Comment(LineBreak='false', Label='CW_0256ms'))
	ks.add(ksm.ChannelRemoval(Channels=[1,5,9,13,17],KeepSpecified='true'))
	ks.add(ksm.Writer(RelativeDirectory='CW_0256ms'))

Write out the resulting configuration:

	ks.write()
	
Run the script:

	ks.run(src="input_dir", dst="output_dir")

The list of modules and their parameters can be found in the
[configuration/korona-info.json](configuration/korona-info.json) file. 
