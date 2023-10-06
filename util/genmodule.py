'''
Parse configuration and generate the necessary classes, and generates
a Modules.py containing class definitions and configurations.
'''

import json

with open('./configuration/korona-info.json', 'r') as f:
    config = json.load(f)

def disclaimer(f):
    f.write('# Auto-generated, do not edit directly\n')
    f.write('# see genmodule.py\n')

with open('./KoronaScript/Configuration.py', 'w') as f:
    disclaimer(f)
    modspec = {}
    
    # write global_spec and modules_spec
    for m in config['modules']:
        name = m['id'][:-6]
        desc = m['description']
        params = m['parameters']

        par = {}
        for p in params:
            if 'defaultValue' in p.keys():
                par[p['id']] = p['defaultValue']
            elif 'parameters' in p.keys():
                par[p['id']] = p['parameters']
            else:
                par[p['id']] = None
            
        # build the dict and then print it?
            modspec[name] = par

    f.write('modules_spec = ')
    f.write(str(modspec)+'\n')
        
with open('./KoronaScript/Modules.py', 'w') as f:
    disclaimer(f)
    
    f.write('from .Configuration import modules_spec\n')
    f.write('from .KoronaModule import KoronaModule\n\n')
    # Output the list of classes, one for each module
    for m in config['modules']:
        name = m['id'][:-6] # chop off "Module"
        desc = m['description']
        params = m['parameters']

        f.write(f'class {name}(KoronaModule):\n')
        f.write(f'    """{desc}"""\n')
        f.write('    def __init__(self, **parameters):\n')
        f.write(f'        super().__init__(\'{name}\', **parameters)\n\n')

        
