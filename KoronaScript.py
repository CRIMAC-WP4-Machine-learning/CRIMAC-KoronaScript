# Class to represent and run a sequence of Korona module applications
# Example usage:
#    ks = KoronaScript(global parameters)
#    ks.add(KoronaModule(parametres)
#    ks.add...
#    ks.write(path)
#    ks.run()

import subprocess
import tempfile
import os
import sys

class KoronaScript():
    '''Construct, store, and run a set of Korona modules'''

    def __init__(self, **parameters): # global parameters
        self._module_list = []
        self._config = global_spec
        for k in parameters:
            if k not in global_spec:
                print(f'Unknown global parameter "{k}" - aborting')
                exit -1
            self._config[k] = parameters[k]

    def add(self, module):
        '''Add a module to the script'''
        self._module_list.append(module)
        return self

    def write(self, cfs=sys.stdout, cds=sys.stdout):
        '''Write the cds and cfs files'''
        cfs.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        cfs.write('<ConfigFiles context="Korona">\n')
        cfs.write('<parameter name="ModuleConfiguration" ref="CfsDirectory">CW.cds</parameter>\n')
        for k,v in self._config.items():
            if v is None:
                cfs.write(f'    <parameter name="{k}"/>\n')
            else:
                cfs.write(f'    <parameter name="{k}">{v}</parameter>\n')
        cfs.write('</ConfigFiles>\n')

        cds.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        cds.write('<ModuleContainer version="3">\n')
        for m in self._module_list:
            cds.write(m.to_xml())
        cds.write('</ModuleContainer>\n')

    def run(self):
        '''Save the files (to /tmp?) and call Korona to execute them'''
        cds, cdsname = tempfile.mkstemp(suffix='.cds')
        cfs, cfsname = tempfile.mkstemp(suffix='.cfs')
        with os.fdopen(cds, 'w') as cdsfd:
            with os.fdopen(cfs, 'w') as cfsfd:
                self.write(cfs=cfsfd, cds=cdsfd)

                # Call this program
                # "$JAVA" $JAVA_OPTS "-Xmx${MAX_MEMORY_MB}m" -classpath "$TOP_INSTALLATION_DIR/lib/jar/*" "-Djava.library.path=$JAVA_LIBRARY_PATH" "-Djna.library.path=$JAVA_LIBRARY_PATH" -XX:-UseGCOverheadLimit -XX:-OmitStackTraceInFastThrow -Dno.marec.incubator=true no.imr.korona.main.KoronaCliMain "$@"
                # subprocess.run(...)


class KoronaModule():
    '''Baseclass for modules'''

    def __init__(self, name, **parameters):
        '''initialize with parameter definitions'''
        # check that the module exists
        if name not in modules_spec:
            print(f'Unknown Korona module "{name}" - aborting')
            exit -1
        self._name = name
        self._config = modules_spec[name]
        for k in parameters:
            if not k in modules_spec[name]:
                print(f'Parameter "{k}" not valid for Korona module "{name}" - aborting')
                exit -1
            self._config[k] = parameters[k]

    def to_xml(self):
        '''Generate XML output'''
        res = ''
        myname = self._name + 'Module'
        res += (f'  <module name="{myname}">\n')
        res += ('    <parameters>\n')
        for k in self._config:
            if self._config[k] is None:
                res += (f'      <parameter name="{k}"/>\n')
            else:
                res += (f'      <parameter name="{k}">{self._config[k]}</parameter>\n')
        res += ('    </parameters>\n')
        res += ('  </module>\n')
        return res

# Example module - can probably be generated automatically?
class NetCdfWriter(KoronaModule):
    '''Korona module to write acoustic data to NetCDF file format'''
    def __init__(self, **parameters):
        super().__init__('NetCdfWriter', **parameters)

class ChannelDataRemoval(KoronaModule):
    '''Korona module to write acoustic data to NetCDF file format'''
    def __init__(self, **parameters):
        super().__init__('ChannelDataRemoval', **parameters)
        
global_spec = {
    # 'ModuleConfiguration' : None, # cds file name, attrib 'ref' points to...what?
    #   <parameter name="ModuleConfiguration" ref="CfsDirectory">CW.cds</parameter>
    'Categorization' : None,
    'HorizontalTransducerOffsets' : None,
    'VerticalTransducerOffsets' : None,
    'TransducerRanges' : None,
    'Plankton' : None,
    'BroadbandNotchFilters' : None,
    'PulseCompressionFilters' : None,
    'BroadbandSplitterBands' : None,
    'Towfish' : None,
}

# Dictionary of modules with parameters and default values
# Maybe list allowed values?        
modules_spec = {
    'NetCdfWriter' : {
        'Active' : 'true',  # is this valid for all modules?
        'DirName' : 'sv',
        'MainFrequency' : '38',
        'DeltaRange' : None,
        'MaxRange' : None,
        'OutputType' : 'SV_AND_ANGLES',
        'WriteAngels' : 'true',
        'FftWindowSize' : '10',
        'DeltaFrequency' : '1',
    },
    'ChannelDataRemoval' : {
        'Active' : 'true',
        'Channels' : None,
        'ChannelsFromEnd' : None,
        'Frequencies' : None,
        'KeepSpecified' : 'true'
    }
}
