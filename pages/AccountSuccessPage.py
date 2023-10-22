import allure
from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from utils.logger import logger


class AccountSuccessPage(BasePage):

    # Locators
    account_creation_success_message = (By.XPATH, "//div[@id='content']/h1")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Get account creation success message step...")
    def get_account_creation_success_message(self) -> str:
        logger.info("Get account creation success message text")
        return self.get_element_text(self.account_creation_success_message)