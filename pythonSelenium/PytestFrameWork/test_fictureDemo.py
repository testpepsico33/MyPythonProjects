import pytest

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixturedemo(self):
       print("I will execute step in fixturedemo method")

    def test_fixturedemo1(self):
       print("I will execute step in fixturedemo1 method")

    def test_fixturedemo2(self):
       print("I will execute step in fixturedemo2 method")

    def test_fixturedemo3(self):
       print("I will execute step in fixturedemo3 method")