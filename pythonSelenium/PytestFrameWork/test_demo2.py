#Any pytest file should starts with test_
#Pytest method name should always starts with "test_"
#Any code should wrapped in method only

import pytest

@pytest.mark.smoke  #smoke is a cstome maek
@pytest.mark.skip #skip is a pre defined mark
def test_firstProgram():
    msg ="Hello"
    assert msg == 'Hi', "Test failed because strings do not match"

def test_secondCreditCard():
    a=4
    b=6
    assert a+2 == b, "Addition does not match"



