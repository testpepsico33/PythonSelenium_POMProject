import pytest
from selenium import webdriver

from utilities import ReadConfigurations

import pytest

import pytest

"""
@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        pass


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep
"""

@pytest.fixture
def setup_and_teardown(request):
    # assigning browser values for config.ini
    browser = ReadConfigurations.readConfigurations("basic info", "browser")
    # from "config" category and key names have to pass
    driver = None
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print("Provide a valid browser name from this list chrome/firefox/edge")
    driver.maximize_window()
    # assigning url values for config.ini
    app_url = ReadConfigurations.readConfigurations("basic info",
                                                    "url")  # from "config" category and key names have to pass
    driver.get(app_url)
    request.cls.driver = driver
    yield
    driver.quit()
