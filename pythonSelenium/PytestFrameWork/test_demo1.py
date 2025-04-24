#Any pytest file should starts with test_
#Pytest method name should always starts with "test_"
#Any code should wrapped in method only

import pytest

@pytest.mark.smoke
def test_firstProgram():
    print("Hello Arav")

@pytest.mark.xfail
def test_SecondGreetCreditCard():
    print("Welcome")