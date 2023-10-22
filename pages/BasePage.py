from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.logger import logger


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def enter_text(self, locator, text) -> None:
        # use * to unpack the positional *args
        logger.info("Enter text into a textbox field")
        self.driver.find_element(*locator).send_keys(text)

    def clear_text(self, locator) -> None:
        logger.info("Clear text from a textbox field")
        self.driver.find_element(*locator).click()
        self.driver.find_element(*locator).clear()

    def click_element(self, locator) -> None:
        logger.info("Click on element")
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(expected_conditions.element_to_be_clickable(self.driver.find_element(*locator)))
        self.driver.find_element(*locator).click()

    def check_element_is_displayed(self, locator) -> bool:
        logger.info("Check if element status is displayed")
        return self.driver.find_element(*locator).is_displayed()

    def get_element_text(self, locator) -> str:
        logger.info("Get element text")
        return self.driver.find_element(*locator).text
