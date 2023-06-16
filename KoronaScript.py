# Class to represent and run a sequence of Korona module applications
# Example usage:
#    ks = KoronaScript(global parameters)
#    ks.add(KoronaModule(parametres)
#    ks.add...
#    ks.write(path)
#    ks.run()

class KoronaScript():
    '''Construct, store, and run a set of Korona modules'''

    def __init__(self): # global parameters
        self._module_list = []
        pass

    def add(self, module):
        '''Add a module to the script'''
        self._module_list.append(module)
        pass

    def write(self, filepath):
        '''Write the cds and xxx files'''
        pass

    def run(self):
        '''Save the files (to /tmp?) and call Korona to execute them'''
        pass

# Example module - can probably be generated automatically?    
class NetCdfWriter(filepath):
    '''Korona module to write acoustic data to NetCDF file format'''
    
    def __init__(self):
        pass
