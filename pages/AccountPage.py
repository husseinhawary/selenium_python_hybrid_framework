import allure
from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from utils.logger import logger


class AccountPage(BasePage):

    # Locators
    edit_your_account_information_link_text = (By.LINK_TEXT, "Edit your account information")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Check edit account information link text displayed on not step...")
    def check_edit_account_information_link_text_display_status(self) -> bool:
        logger.info("Check edit account information link text status is displayed")
        return self.check_element_is_displayed(self.edit_your_account_information_link_text)