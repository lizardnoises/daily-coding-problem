__author__ = 'Sean Moore'

from problem082 import *
import pytest

@pytest.mark.parametrize('fileName,expected', [
    ('example', 'Hello w')
])
def testRead7(fileName, expected):
    with open(fileName, 'r') as f:
        assert read7(f) == expected

@pytest.mark.parametrize('fileName,n,expected', [
    ('example', 5, 'Hello')
])
def testReadN(fileName, n, expected):
    with open(fileName, 'r') as f:
        assert readN(f, n) == expected