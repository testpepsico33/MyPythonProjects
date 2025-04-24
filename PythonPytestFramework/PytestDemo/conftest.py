import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executed first")
    yield
    print("I will execute last")

#loading data when we wants to send data to test case which needs its
@pytest.fixture()
def dataLoad():
    print("user profile data being created")
    return ["Nirmal","Kumar","google.com"]

@pytest.fixture()
def testing():
    print("Testing 1")
    return ["Arav","Nirmal","Soniya"]

#Parameterizing
#@pytest.fixture(params=[("chrome","Nirmal","Arav","Soniya"),("firefox","Arav"),("IE","Soniya")])
@pytest.fixture(params=["chrome","firefox","IE"])
def crossBrowser(request):
    return request.param

