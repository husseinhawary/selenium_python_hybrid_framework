from datetime import datetime

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver

from utils import ReadConfigurations
from utils.logger import logger


# passing options from pytest commands, so I will pass the browser name
def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def setup_and_teardown(request):
    logger.info("\nBrowser setup based on browser value which passed in the command line during executing the scripts")
    # browser = ReadConfigurations.read_configurations("basic_info", "browser")
    browser = request.config.getoption("--browser")
    logger.info(f"Browser name is {browser}")
    global driver
    # driver = None
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("chrome-headless"):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--disable-popup-blocking")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        # options.add_argument('--ignore-certificate-errors')
        # options.add_argument("--disable-blink-features=AutomationControlled")
        # options.add_argument("--start-maximized")
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options=options)
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        raise Exception(f"Browser {browser} isn't supported yet!")
    driver.maximize_window()
    logger.info("Read app_url value from configurations/config.ini file")
    app_url = ReadConfigurations.read_configurations("basic_info", "url")
    driver.get(app_url)
    request.cls.driver = driver
    yield
    logger.info(f"\nClose {browser} driver after test")
    driver.quit()


# # This method to take screenshot on failure and as a helper for this fixture log_on_failure
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


# This fixture will take screenshot on failure
@pytest.fixture()
def log_on_failure(request):
    logger.info("This fixture will take screenshot on failure")
    yield
    item = request.node
    if item.rep_call.failed:
        file_name = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S_%F')}" \
            .replace("/", "_").replace("::", "__")
        capture_path = f"./screenshots/{file_name}.png"
        driver.save_screenshot(capture_path)
        allure.attach(
            driver.get_screenshot_as_png(),
            name=f'screenshot {file_name}',
            attachment_type=AttachmentType.PNG
        )



