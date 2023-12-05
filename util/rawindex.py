import sys
import struct
import mmap

# text colors: GREEN = '\033[92m', BLUE = '\033[94m', HEADER = '\033[95m', CYAN = '\033[96m', BOLD = '\033[1m', UNDERLINE = '\033[4m'
#              CLEAR = '\033[0m', YELLOW = '\033[93m', RED = '\033[91m'

def warn(*args, **kwargs):
    print('\033[93mWarning\033[0m',*args, file=sys.stderr, **kwargs)

def error(*args, **kwargs):
    print('\033[91mError:\033[0m',*args, file=sys.stderr, **kwargs)

import util.simrad_parsers as sp
def parse(str):
    '''Table for selecting the correct parser to use for datagrams'''
    # duplicates the simrad_raw_file.DGRAM_TYPE_KEY, but with bytestring keys
    parsers = {
          b'BOT' : sp.SimradBottomParser()
        , b'CON' : sp.SimradConfigParser()
        , b'DEP' : sp.SimradDepthParser()
        , b'FIL' : sp.SimradFILParser()
        , b'MRU' : sp.SimradMRUParser()
        , b'NME' : sp.SimradNMEAParser()
        , b'RAW' : sp.SimradRawParser()
        , b'TAG' : sp.SimradAnnotationParser()
        , b'XML' : sp.SimradXMLParser()
    }

    dgram_type = str[:3]
    p = parsers[dgram_type]
    return(p.from_string(str, len(str)))

def index(f):
    '''Build an index of datagrams in a Simrad RAW file.  This is a list of position, type, length, and (unparsed) contents.'''
    idx = []
    with open(f, "rb") as fh:
        with mmap.mmap(fh.fileno(), length=0, access=mmap.ACCESS_READ) as mf:
            position = 0
            while position < len(mf):
                length, msg = struct.unpack('<l4s', mf[position:position+8])
                if position+length > len(mf):
                    raise Exception('Premature EOF, truncated RAW file?')
                v = struct.unpack('<l', mf[position+length+4:position+length+8])
                t = msg.decode('latin-1')
                if v[0] != length: warn(
                    f'Datagram at {position}: control lenght mismatch ({length} vs {v[0]}) - endianness error or corrupt file?')
                idx.append((position, t, length, mf[position + 4:position + 4 + length]))
                position += length + 8

    return idx

if __name__ == '__main__':
    # just print the index of datagrams
    for pos,typ,length,msg in index(sys.argv[1]):
        print(f'{typ}\t{length}')


