from sort import selectSort
import pytest
def test_sortnum():
    assert selectSort([65,3,1,6,8,9,5]) == [1,3,5,6,8,9,65]

def test_sortstr():
    assert selectSort(['c','a','b']) == ['a','b','c']

def test_sorterror():
    with pytest.raises(TypeError):
        selectSort(8952431)