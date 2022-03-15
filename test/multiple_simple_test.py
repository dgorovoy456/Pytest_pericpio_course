import pytest


# @pytest.mark.number
def test_type():
    assert type(1 + 2) is int


# @pytest.mark.number
def test_add_int():
    assert 5 + 2 == 9


@pytest.mark.skip(reason='Temporarily disabled')
# @pytest.mark.string
def test_string():
    assert 'u' in 'sun'


# @pytest.mark.string
def test_add_string():
    assert ('sunny ' + 'day') == 'sunny day'
