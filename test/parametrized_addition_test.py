import src.cal as cal
import pytest


@pytest.mark.parametrize('input1, input2, result',
                         [(1, 2, 3),
                          (5.2, 2.4, 7.6),
                          ('winter ', 'season', 'winter season')])
def test_add(input1, input2, result):
    assert cal.add(input1, input2) == result

