import allure
from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from utils.logger import logger


class SearchPage(BasePage):

    # Locators
    product_link_text = (By.LINK_TEXT, "HP LP3065")
    no_product_message = (By.XPATH, "//input[@id='button-search']/following-sibling::p")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Check product title status if displayed or not step...")
    def check_product_title_display_status(self) -> bool:
        logger.info("check product title display status")
        return self.check_element_is_displayed(self.product_link_text)

    @allure.step("Get no product warning message step...")
    def get_no_product_message_text(self) -> str:
        logger.info("Get no product message text")
        return self.get_element_text(self.no_product_message)
