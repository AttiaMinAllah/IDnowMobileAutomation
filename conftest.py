import sys
import os
import pytest
import json
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions

print("sys.path:", sys.path)  # For debugging

def pytest_addoption(parser):
    parser.addoption(
        "--platform", action="store", default="android", help="platform to run tests on: android or ios"
    )

@pytest.fixture(scope="module")
def ident_ids():
    test_data_path = os.path.join(os.path.dirname(__file__), 'common', 'test_data.json')
    with open(test_data_path) as f:
        test_data = json.load(f)
    return test_data["ident_ids"]

@pytest.fixture(scope="module")
def driver(pytestconfig):
    platform = pytestconfig.getoption("platform")
    print(f"Running tests on platform: {platform}")  # For debugging

    if platform == 'android':
        options = UiAutomator2Options()
        options.platform_name = 'Android'
        options.device_name = 'emulator-5554'
        options.app = '/Users/attiaminallah/Documents/IDnowMobileAutomation/app-release-signed-534.apk'
        options.automation_name = 'UiAutomator2'

        driver = webdriver.Remote('http://localhost:4723', options=options)
    elif platform == 'ios':
        options = XCUITestOptions()
        options.platform_name = 'iOS'
        options.device_name = 'iPhone Simulator'
        options.app = 'AutoIdent.ipa'
        options.automation_name = 'XCUITest'

        driver = webdriver.Remote('http://localhost:4723', options=options)
    else:
        raise ValueError("Unsupported platform: {}".format(platform))

    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def home_page(driver, pytestconfig):
    platform = pytestconfig.getoption("platform")
    if platform == 'android':
        from android.pages.home_page import HomePage
    elif platform == 'ios':
        from ios.pages.home_page import HomePage
    return HomePage(driver)