import pytest

from PytestDemo.BaseClass import BaseClass


@pytest.mark.usefixtures
class Testloaddata(BaseClass):
    def test_editProfile(self,dataLoad):
        log=self.getLogger()
        log.info(dataLoad[0])
        log.info(dataLoad[2])


