import pytest

from ex_hm_classes.hw.ex4 import MyDict


def test_init():
    mydict = MyDict([('one', 1), ('two', 2), ('three', 3)])
    assert mydict.one == 1

    with pytest.raises(AttributeError):
        mydict.test == 1
