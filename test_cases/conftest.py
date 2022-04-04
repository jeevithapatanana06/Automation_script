import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    global driver
    if browser=='edge':
        driver=webdriver.Edge("C:\\edgedriver_win64\\msedgedriver.exe")
        print("Launching chrome browser.........")
    elif browser=='firefox':
        driver = webdriver.Firefox("C:\\geckodriver-v0.30.0-win64\\geckodriver.exe")
        print("Launching firefox browser.........")
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