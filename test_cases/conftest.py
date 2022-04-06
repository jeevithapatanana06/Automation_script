import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    global driver
    if browser=='edge':
        driver=webdriver.Edge("C:\\edgedriver_win64\\msedgedriver.exe")
        print("Launching chrome browser.........")
    elif browser=='chrome':
        driver = webdriver.Chrome("C:\\chromedriver_win32 (1)\\chromedriver.exe")
        print("Launching chrome browser.........")
    return driver

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


def pytest_configure(config):

     config._metadata["project name"] = 'Test-Application'
     config._metadata['module name'] = 'Customers app'
     config._metadata['tester'] = 'Jeevitha'