
from rle import rle
from rld import rld

def test_rle():
    assert rle('kkk') == '3k'

def test_rle2():
    assert rle('kkkkkkkkkkkkoooo') == '12k4o'

def test_empty():
    assert rle('') == "no input"
    
def test_rld_empty():
    assert rld('') == "no input"

def test_rld_single():
    assert rld('2k') == "kk"
    
def test_rld_double():
    assert rld('2k4a') == "kkaaaa"