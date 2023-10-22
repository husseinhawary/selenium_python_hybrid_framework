import allure
import pytest
from pages.HomePage import HomePage
from utils.logger import logger
from utils.utils import json_data_reader


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.usefixtures("setup_and_teardown", "log_on_failure")
class TestSearch:

    @pytest.fixture()
    def open_home_page(self):
        logger.info("Open home page fixture")
        yield HomePage(self.driver)

    @pytest.fixture()
    def read_search_data_from_json_file(self):
        logger.info("Read search data from json file fixture")
        data = json_data_reader("test_data/search_data.json")
        yield data

    def test_search_for_a_valid_product(self, open_home_page, read_search_data_from_json_file):
        logger.info("Test search with valid product name")
        home_page = open_home_page
        data = read_search_data_from_json_file
        valid_product_name = data["valid_search_value"]
        search_page = home_page.search_for_a_product(valid_product_name)
        assert search_page.check_product_title_display_status()

    def test_search_for_an_invalid_product(self, open_home_page, read_search_data_from_json_file):
        logger.info("Test search with invalid product name")
        home_page = open_home_page
        data = read_search_data_from_json_file
        invalid_product_name = data["invalid_search_value"]
        search_page = home_page.search_for_a_product(invalid_product_name)
        expected_result = "There is no product that matches the search criteria."
        assert search_page.get_no_product_message_text().__eq__(expected_result)

    def test_search_without_providing_any_product(self, open_home_page):
        logger.info("Test search with empty product name")
        home_page = open_home_page
        search_page = home_page.search_for_a_product("")
        expected_result = "There is no product that matches the search criteria."
        assert search_page.get_no_product_message_text().__eq__(expected_result)
