import src.exeptions as ex
import pytest


def test_divide_pass():
    assert ex.divide(18, 2) == 9


def test_divide_error_zero():
    with pytest.raises(ZeroDivisionError):
        ex.divide(18, 0) == 9


def test_divide_error_type():
    with pytest.raises(TypeError):
        ex.divide(18, 'a') == 9
