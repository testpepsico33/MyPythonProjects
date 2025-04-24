import pytest


@pytest.mark.smoke
def test_sample_file_one():
    print("Testing,test_sample_file_one")
@pytest.mark.regression
def test_sample_file_two():
    print("Testing,test_sample_file_two")
@pytest.mark.smoke
def test_sample_file_three():
    print("Testing,test_sample_file_three")
@pytest.mark.sanity
def test_sample_file_eleven():
    print("Testing,test_sample_file_eleven")

def test_sample_file_twelve():
    print("Testing,test_sample_file_twelve")