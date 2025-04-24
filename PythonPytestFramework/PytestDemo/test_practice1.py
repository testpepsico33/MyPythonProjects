import pytest


@pytest.mark.usefixtures
class Test_testingclass:
    def test_python(self,testing):
        print(testing)
