import pytest
from selenium import webdriver


@pytest.fixture
def setup(browser):
    if browser == "chrome":
        print("launching chrome browser")
        return webdriver.Chrome()
    elif browser == "firefox":
        print("launching firefox browser")
        return webdriver.Firefox()
    else:
        return webdriver.Chrome()


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


# It is hook for add/delete Environment info to HTML Report
@pytest.hookimpl(tryfirst=True)
def pytest_metadata(metadata):
    metadata['Project Name'] = "OrangrHRM"
    metadata['Module Name'] = "Customers"
    metadata['tester'] = "Dnyaneshvar"
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
