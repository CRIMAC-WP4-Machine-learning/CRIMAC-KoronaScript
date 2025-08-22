import os
import urllib.request as ftp

import examples.channelRemoval as CR

TESTDATA = os.path.join('test_data', 'EK60')
URL = 'ftp://ftp.ngdc.noaa.gov/pub/outgoing/mgg/wcd/pyEcholab_data/examples/EK60'

def test_get_data():
    os.makedirs(TESTDATA, exist_ok=True)
    for suffix in ['bot', 'idx', 'raw']:
        for it in ['DY1201_EK60-D20120214-T231011', 'DY1706_EK60-D20170609-T005736']:
            fname = it + '.' + suffix
            fullname = os.path.join(TESTDATA, fname)
            if not os.path.exists(fullname):
                print(f'Fetching: {fname}')
                ftp.urlretrieve(f'{URL}/{fname}', fullname)

def test_channelRemoval():
    """This fails to fail if no data is present"""
    CR.ks.run('test_data/EK60', 'test_out/cr_out')
