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
                exit(-1)
            self._config[k] = parameters[k]

    def add(self, module):
        '''Add a module to the script'''
        self._module_list.append(module)
        return self

    def write(self, cfs=sys.stdout, cds=sys.stdout, cdsname=None):
        '''Write the cds and cfs files'''
        cfs.write('<?xml version="1.0" encoding="UTF-8"?>\n\n')
        cfs.write('<ConfigFiles context="Korona">\n')
        cfs.write(f'    <parameter name="ModuleConfiguration" ref="CfsDirectory">{cdsname}</parameter>\n')
        for k,v in self._config.items():
            if v is None:
                cfs.write(f'    <parameter name="{k}"/>\n')
            else:
                cfs.write(f'    <parameter name="{k}">{v}</parameter>\n')
        cfs.write('</ConfigFiles>\n')

        cds.write('<?xml version="1.0" encoding="UTF-8"?>\n\n')
        cds.write('<ModuleContainer version="3">\n')
        cds.write('  <modules>\n')
        for m in self._module_list:
            cds.write(m.to_xml())
        cds.write('  </modules>\n')
        cds.write('</ModuleContainer>\n')

    def run(self, src, dst):
        '''Save the files (to /tmp?) and call Korona to execute them'''
        cfs, cfsname = tempfile.mkstemp(suffix='.cfs')
        cds, cdsname = tempfile.mkstemp(suffix='.cds')
        with os.fdopen(cds, 'w') as cdsfd:
            with os.fdopen(cfs, 'w') as cfsfd:
                self.write(cfs=cfsfd, cds=cdsfd, cdsname=cdsname)

        # if os.getenv('JAVA_HOME'): (...)
        lsss = os.getenv('LSSS')
        if lsss is None:
            print('LSSS environment variable not specified')
            exit(-1)
        os.environ['TOP_INSTALLATION_DIR'] = lsss

        java = lsss+'/jre/bin/java'

        # "-Xmx${MAX_MEMORY_MB}m" -classpath "$TOP_INSTALLATION_DIR/lib/jar/*" "-Djava.library.path=$JAVA_LIBRARY_PATH" "-Djna.library.path=$JAVA_LIBRARY_PATH" -XX:-UseGCOverheadLimit -XX:-OmitStackTraceInFastThrow -Dno.marec.incubator=true no.imr.korona.main.KoronaCliMain "$@"
        javaopts = ['-classpath', f'{lsss}/lib/jar/*', '-Dno.marec.incubator=true', 'no.imr.korona.main.KoronaCliMain']
        res = subprocess.run([java] + javaopts + ['batch', '--cfs', cfsname, '--source', src, '--destination', dst])
        print(res.stdout)
        if res.returncode != 0:
            print('Warning: Java subprocess returned error code {res.returncode}')
            print('Errors:')
            print(res.stderr)

class KoronaModule():
    '''Baseclass for modules'''

    def __init__(self, name, **parameters):
        '''initialize with parameter definitions'''
        # check that the module exists
        if name not in modules_spec:
            print(f'Unknown Korona module "{name}" - aborting')
            exit(-1)
        self._name = name
        self._config = modules_spec[name]
        for k in parameters:
            if not k in modules_spec[name]:
                print(f'Parameter "{k}" not valid for Korona module "{name}" - aborting')
                exit(-1)
            self._config[k] = parameters[k]

    def to_xml(self):
        '''Generate XML output'''
        res = ''
        myname = self._name + 'Module'
        res += (f'  <module name="{myname}">\n')
        res += ('    <parameters>\n')
        for k in self._config:
            if self._config[k] is None:
                res += f'      <parameter name="{k}"/>\n'
            elif isinstance(self._config[k],list):
                res += f'      <parameter name="{k}">'
                for v in self._config[k]:
                    res += str(v)+','
                res = res[:-1] # remove last comma
                res += '</parameter>\n'
            elif isinstance(self._config[k],dict):
                res += f'      <parameter name="{k}">\n'
                # Should maybe call recursively?  Can they be lists or dicts?
                for key,val in self._config[k].items():
                    res += f'       <parameter name="{key}">{val}</parameter>\n'
                res +=  '      </parameter>\n'
            else:
                res += (f'      <parameter name="{k}">{self._config[k]}</parameter>\n')
        res += ('    </parameters>\n')
        res += ('  </module>\n')
        return res

# Example module - can probably be generated automatically?
class NetcdfWriter(KoronaModule):
    '''Korona module to write acoustic data to NetCDF file format'''
    def __init__(self, **parameters):
        super().__init__('NetcdfWriter', **parameters)

class ChannelDataRemoval(KoronaModule):
    '''Korona module to remove channel data, maybe?'''
    def __init__(self, **parameters):
        super().__init__('ChannelDataRemoval', **parameters)

class ChannelRemoval(KoronaModule):
    '''Korona module to remove channels?'''
    def __init__(self, **parameters):
        super().__init__('ChannelRemoval', **parameters)

class Writer(KoronaModule):
    '''Korona module to write acoustic data to RAW file format'''
    def __init__(self, **parameters):
        super().__init__('Writer', **parameters)

class Comment(KoronaModule):
    '''Korona module for comments'''
    def __init__(self, **parameters):
        super().__init__('Comment', **parameters)

class TemporaryComputationsBegin(KoronaModule):
    '''Korona module for... something?'''
    def __init__(self, **parameters):
        super().__init__('TemporaryComputationsBegin', **parameters)

class TemporaryComputationsEnd(KoronaModule):
    '''Korona module for... something?'''
    def __init__(self, **parameters):
        super().__init__('TemporaryComputationsEnd', **parameters)

class EmptyPingRemoval(KoronaModule):
    '''Korona module for removing empty pings, I guess.'''
    def __init__(self, **parameters):
        super().__init__('EmptyPingRemoval', **parameters)

class Tracking(KoronaModule):
    '''Korona module for tracking single targets'''
    def __init__(self, **parameters):
        super().__init__('Tracking', **parameters)

        
global_spec = {
    # 'ModuleConfiguration' : None, # cds file name, attrib 'ref' points to...what?
    #   <parameter name="ModuleConfiguration" ref="CfsDirectory">CW.cds</parameter>
    # The following are None, or point to xml files (contents unknown)
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
# Maybe list allowed values?  All modules have a parameter 'active',
# which can be true, or, presumably, false
modules_spec = {
    'Comment' : {
        'Active' : 'true',
        'LineBreak' : 'false',
        'VerticalSpace' : None, # 8
        'Label' :  None,  # 'CW_0256ms'
        'Comment' : None
    },
    'NetcdfWriter' : {
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
    'Writer' : {
        'Active' : 'true',
        'FileName' : None,
        'UseRelativeDirectory' : 'true',
        'RelativeDirectory' : None # 'CW_0256ms'
    },
    'ChannelDataRemoval' : {
        'Active' : 'true',
        'Channels' : None,
        'ChannelsFromEnd' : None,
        'Frequencies' : None,
        'KeepSpecified' : 'true'
    },
    # This is the same as ChannelDataRemoval - why?
    'ChannelRemoval' : {
        'Active' : 'true',
        'Channels' : None, # or list of channels (ints)
        'ChannelsFromEnd' : None,
        'Frequencies' : None,
        'KeepSpecified' : 'true'
    },
    'TemporaryComputationsBegin' : {
        'Active' : 'true'
    },
    'TemporaryComputationsEnd' : {
        'Active' : 'true'
    },
    'EmptyPingRemoval' : {
        'Active' : 'true'
    },
    'Tracking' : {
        'Active' : 'true',
        'TrackerType' : 'SED',
        'kHz' : '333',
        'PlatformMotionType' : 'Floating',
        'MinTS' : '-50',
        'PulseLengthDeterminationLevel' : '5',
        'MinEchoLength' : '0.005',
        'MaxEchoLength' : '0.15',
        'MaxGainCompensation' : '4',
        'DoPhaseDeviationCheck' : 'true',
        'MaxPhaseDevSteps' : '8',
        'MaxTS' : '-20',
        'MaxDepth' : '25.3',
        'MaxAlongshipAngle' : '5',
        'MaxAthwartshipAngle' : '5',
        'InitiationGateFunction' : {
            'Alpha' : '2.8',
            'Beta' : '2.8',
            'Range' : '0.1',
            'TS' : '20'
        },
        'InitiationMinLength' : '1',
        'GateFunction' : {
            'Alpha' : '2.8',
            'Beta' : '2.8',
            'Range' : '0.1',
            'TS' : '20'
        },
        'AlphaBetaEstimator' : {
            'Alpha' : '0.5',
            'Beta' : '0.5'
        },
        'MaxMissingPings' : '4',
        'MaxMissingSamples' : '2',
        'MaxMissingPingsFraction' : '0.7',
        'MinTrackLength' : '12',
        'MinSampleToLengthFraction' : '1'
    }
}
