import pytest
@pytest.fixture(autouse=True, scope="session")
def setup_and_teardown(): #setup code which can be run before the test method code
    print("launch Browser")
    print("Open application URL in browser")
    yield  #teardown code which can be run after the test method code
    print("Logout from application")
    print("Close the browser")