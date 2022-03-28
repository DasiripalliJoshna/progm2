import Prism
import pytest

def test_surface_prism():
    l=2
    b=3
    h=4
    result=Prism.surface_prism(l,b,h)
    assert result == 2*((l*b) + (l*h) + (b*h))

def test_volume_prism():
    l = 2
    b = 3
    h = 4
    result =Prism.volume_prism(l, b, h)
    assert result == l*b*h

def test_diaganol_prism():
    l = 2
    b = 3
    h = 4
    diaganal = ((l * l) + (b * b )+ (h * h))
    result = Prism.diaganol_prism(l, b, h)
    assert result == diaganal ** 0.5