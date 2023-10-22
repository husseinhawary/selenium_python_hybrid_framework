import time

import allure
from selenium.webdriver.common.by import By
from pages.AccountSuccessPage import AccountSuccessPage
from pages.BasePage import BasePage
from utils.logger import logger


class RegisterPage(BasePage):
    # Locators
    first_name_text_box = (By.ID, "input-firstname")
    last_name_text_box = (By.ID, "input-lastname")
    email_text_box = (By.ID, "input-email")
    telephone_text_box = (By.ID, "input-telephone")
    password_text_box = (By.ID, "input-password")
    password_confirm_text_box = (By.ID, "input-confirm")
    policy_privacy_checkbox = (By.NAME, "agree")
    continue_button = (By.XPATH, "//input[@value='Continue']")
    yes_newsletter_radio_button = (By.XPATH, "//div[@id='content']/h1")
    invalid_register_warning_message = (By.XPATH, "//div[contains(@class, 'alert-danger')]")
    first_name_warning_message = (By.XPATH, "//input[@id='input-firstname']/following-sibling::div")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Enter first name with value first_name: {0} step...")
    def enter_first_name(self, first_name) -> None:
        logger.info("Enter first name in user register page")
        self.clear_text(self.first_name_text_box)
        self.enter_text(self.first_name_text_box, first_name)

    @allure.step("Enter last name with value last_name: {0} step...")
    def enter_last_name(self, last_name) -> None:
        logger.info("Enter last name in user register page")
        self.clear_text(self.last_name_text_box)
        self.enter_text(self.last_name_text_box, last_name)

    @allure.step("Enter email with value email: {0} step...")
    def enter_email(self, email) -> None:
        logger.info("Enter email in user register page")
        self.clear_text(self.email_text_box)
        self.enter_text(self.email_text_box, email)

    @allure.step("Enter telephone with value telephone: {0} step...")
    def enter_telephone(self, telephone) -> None:
        logger.info("Enter telephone in user register page")
        self.clear_text(self.telephone_text_box)
        self.enter_text(self.telephone_text_box, telephone)

    @allure.step("Enter password with value password: {0} step...")
    def enter_password(self, password) -> None:
        logger.info("Enter password in user register page")
        self.clear_text(self.password_text_box)
        self.enter_text(self.password_text_box, password)

    @allure.step("Enter password_confirm with value password_confirm: {0} step...")
    def enter_password_confirm(self, password_confirm) -> None:
        logger.info("Enter confirm password in user register page")
        self.clear_text(self.password_confirm_text_box)
        self.enter_text(self.password_confirm_text_box, password_confirm)

    @allure.step("Select privacy policy step...")
    def select_privacy_policy_checkbox(self) -> None:
        logger.info("Select privacy policy in user register page")
        self.click_element(self.policy_privacy_checkbox)

    @allure.step("Click on continue button step...")
    def click_on_continue_button(self) -> AccountSuccessPage:
        logger.info("Click on continue button in user register page")
        self.click_element(self.continue_button)
        return AccountSuccessPage(self.driver)

    @allure.step("Select yes news letter step...")
    def select_yes_news_letter(self) -> None:
        logger.info("Select yes news letter in user register page")
        self.click_element(self.yes_newsletter_radio_button)

    @allure.step("Register to the application with first_name: {0}, last_name: {1}, email: {2}, telephone: {3},"
                 "password: {4}, confirm_password: {5}, yes_or_no: {6}, privacy_policy: {7} step...")
    def register_an_account(self, first_name, last_name, email, telephone, password, confirm_password,
                            yes_or_no, privacy_policy) -> AccountSuccessPage:
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email(email)
        self.enter_telephone(telephone)
        self.enter_password(password)
        self.enter_password_confirm(confirm_password)
        if yes_or_no.__eq__("yes"):
            self.select_yes_news_letter()
        if privacy_policy.__eq__("select"):
            self.select_privacy_policy_checkbox()
        return self.click_on_continue_button()

    @allure.step("Get invalid register warning message step...")
    def get_invalid_register_warning_message(self) -> str:
        logger.info("Get invalid user register warning message in user register page")
        return self.get_element_text(self.invalid_register_warning_message)

    @allure.step("Get first name warning message step...")
    def get_first_name_warning_message(self) -> str:
        logger.info("Get invalid first name warning message in user register page")
        return self.get_element_text(self.first_name_warning_message)
