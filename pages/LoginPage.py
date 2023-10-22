import allure
from selenium.webdriver.common.by import By
from pages.AccountPage import AccountPage
from pages.BasePage import BasePage
from utils.logger import logger


class LoginPage(BasePage):

    # Locators
    input_email_text_box = (By.ID, "input-email")
    input_password_text_box = (By.ID, "input-password")
    login_button = (By.XPATH, "//input[@value='Login']")
    warning_message = (By.XPATH, "//div[contains(@class, 'alert-danger')]")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Enter email address with value email_address: {0} step...")
    def enter_email_address(self, email_address) -> None:
        logger.info("Enter email address in login page")
        self.clear_text(self.input_email_text_box)
        self.enter_text(self.input_email_text_box, email_address)

    @allure.step("Enter password with value password: {0} step...")
    def enter_password(self, password) -> None:
        logger.info("Enter password in login page")
        self.clear_text(self.input_password_text_box)
        self.enter_text(self.input_password_text_box, password)

    @allure.step("Click on login button step...")
    def click_on_login_button(self) -> AccountPage:
        logger.info("Click on login button after filling login data")
        self.click_element(self.login_button)
        return AccountPage(self.driver)

    @allure.step("Login to the application with user_email: {0}, user_password: {1} step...")
    def login_to_application(self, user_email, user_password) -> AccountPage:
        self.enter_email_address(user_email)
        self.enter_password(user_password)
        return self.click_on_login_button()

    @allure.step("Get warning message step...")
    def get_warning_message_text(self) -> str:
        logger.info("Get warning message message text in login page")
        return self.get_element_text(self.warning_message)
