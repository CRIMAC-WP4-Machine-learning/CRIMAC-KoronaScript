# Class to represent and run a sequence of Korona module applications
# Example usage:
#    ks = KoronaScript(global parameters)
#    ks.add(KoronaModule(parametres)
#    ks.add...
#    ks.write(path)
#    ks.run()

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

    def write(self, filepath=None):
        '''Write the cds and cfs files'''
        if filepath is None:
            for m in self._module_list:
                print(m._config)
        else:
            print('<?xml version="1.0" encoding="UTF-8"?>')
            print('<ConfigFiles context="Korona">')
            print('<parameter name="ModuleConfiguration" ref="CfsDirectory">CW.cds</parameter>')
            for k,v in self._config.items():
                if v is None:
                    print(f'    <parameter name="{k}"/>')
                else:
                    print(f'    <parameter name="{k}">{v}</parameter>')

            print('----')
            print('<?xml version="1.0" encoding="UTF-8"?>')
            print()
            print('<ModuleContainer version="3">')
            for m in self._module_list:
                m.to_xml()
            print('</ModuleContainer>')    

    def run(self):
        '''Save the files (to /tmp?) and call Korona to execute them'''
        pass

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
        myname = self._name + 'Module'
        print(f'  <module name="{myname}">')
        print('    <parameters>')
        for k in self._config:
            if self._config[k] is None:
                print(f'      <parameter name="{k}"/>')
            else:
                print(f'      <parameter name="{k}">{self._config[k]}</parameter>')
        print('    </parameters>')
        print('  </module>')

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
