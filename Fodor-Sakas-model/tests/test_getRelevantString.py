import pytest
from .. import getRelevanceString

grs = getRelevaceString.getRelevanceString

def test_emptyGSet():
    assert grs([], 2) == ''

def test_oneElementGSet():
    assert grs(['01'], 2) == '01'

def test_badGSet():
    assert grs(['1', '0001'], 4) == None
