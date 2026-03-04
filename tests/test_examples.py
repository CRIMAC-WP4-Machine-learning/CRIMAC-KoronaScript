import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from examples import channelRemoval as CR
from examples import pulseCompression as PC
from examples import tracking as T
from examples import tsDetection as TS

TESTDATA = 'testdata'

def test_channelRemoval():
    """This fails to fail if no data is present"""
    CR.ksi.run(TESTDATA, 'test_out/cr_out')

def test_pulseCompression():
    PC.ksi.run(TESTDATA, 'test_out/pc_out')

def test_tracking():
    """This fails to fail if no data is present"""
    T.ksi.run(TESTDATA, 'test_out/t_out')

def test_tsDetection():
    """This fails to fail if no data is present"""
    TS.ksi.run(TESTDATA, 'test_out/ts_out')
