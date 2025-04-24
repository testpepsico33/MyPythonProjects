from pkgutil import get_data

import openpyxl
import pytest

from utilities import ExcelReader
from utilities.ExcelReader import get_data_from_excel


@pytest.mark.parametrize("username,password", ExcelReader.get_data_from_excel("C://Users//nimalkumar.j//PycharmProjects//DataDrivenTestingWithExcel//ExcelFiles//TutorialsNinja.xlsx",'LoginTest'))
def test_login(username, password):
    print("Logging using username:" + username + "and password: " + password)
