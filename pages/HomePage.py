import allure
from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.LoginPage import LoginPage
from pages.RegisterPage import RegisterPage
from pages.SearchPage import SearchPage
from utils.logger import logger


class HomePage(BasePage):

    # Locators
    search_text_box_field = (By.NAME, "search")
    search_btn = (By.XPATH, "//button[contains(@class,'btn-default')]")
    my_account_dropdown_menu = (By.XPATH, "//a[@title='My Account']")
    login_link_text = (By.LINK_TEXT, "Login")
    register_link_text = (By.LINK_TEXT, "Register")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Enter product to the search box with product_name: {0} step...")
    def enter_product_into_search_text_box_field(self, product_name) -> None:
        logger.info("Enter search value to search text field")
        self.clear_text(self.search_text_box_field)
        self.enter_text(self.search_text_box_field, product_name)

    @allure.step("Click on search button step...")
    def click_on_search_button(self) -> SearchPage:
        logger.info("Click on search button")
        self.click_element(self.search_btn)
        return SearchPage(self.driver)

    @allure.step("Click on my account dropdown list step...")
    def click_on_my_account_dropdown_menu(self) -> None:
        logger.info("open my account dropdown list")
        self.click_element(self.my_account_dropdown_menu)

    @allure.step("Click on login link step...")
    def click_on_login_button(self) -> LoginPage:
        logger.info("Select login from my account dropdown list")
        self.click_element(self.login_link_text)
        return LoginPage(self.driver)

    @allure.step("Open login page step...")
    def navigate_to_login_page(self) -> LoginPage:
        logger.info("Open login page")
        self.click_on_my_account_dropdown_menu()
        return self.click_on_login_button()

    @allure.step("Click on register link step...")
    def click_on_register_button(self) -> RegisterPage:
        logger.info("Select register from my account dropdown list")
        self.click_element(self.register_link_text)
        return RegisterPage(self.driver)

    @allure.step("Open register page step...")
    def navigate_to_register_page(self) -> RegisterPage:
        logger.info("Open register page")
        self.click_on_my_account_dropdown_menu()
        return self.click_on_register_button()

    @allure.step("Search for product with product_name: {0} step...")
    def search_for_a_product(self, product_name) -> SearchPage:
        logger.info("Search on a product")
        self.enter_product_into_search_text_box_field(product_name)
        return self.click_on_search_button()
