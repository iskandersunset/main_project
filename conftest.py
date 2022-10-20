import pytest


@pytest.fixture()
def set_up():
    print("Start TEST")
    yield
    print("Finish TEST")
