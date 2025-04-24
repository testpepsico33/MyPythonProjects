import pytest

@pytest.mark.parametrize("username,password",[("Nirmal","7"),("Arav","7"),("Soniya","4")])
def test_sample_file_seven(username,password):
    print(username)
    print(password)
