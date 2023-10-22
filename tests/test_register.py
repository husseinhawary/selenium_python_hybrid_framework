import allure
import pytest
from pages.HomePage import HomePage
from utils import ExcelDataReader
from utils.logger import logger
from utils.utils import generate_email_with_current_time_stamp, json_data_reader


@pytest.mark.usefixtures("setup_and_teardown", "log_on_failure")
class TestRegister:

    @pytest.fixture()
    def open_register_page(self):
        logger.info("Open user register page fixture")
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        yield register_page

    @pytest.fixture()
    def read_register_data_from_json_file(self):
        logger.info("Read register data from json file fixture")
        data = json_data_reader("test_data/user_registration_data.json")
        yield data

    @allure.severity(allure.severity_level.CRITICAL)
    def test_register_with_mandatory_fields_via_reading_data_from_excel(self, open_register_page):
        logger.info("Test register with mandatory fields and reading data from excel file")
        register_page = open_register_page
        first_name = ExcelDataReader.get_cell_data("test_data/user_data.xlsx", "register_data", 2, 1)
        last_name = ExcelDataReader.get_cell_data("test_data/user_data.xlsx", "register_data", 2, 2)
        telephone = ExcelDataReader.get_cell_data("test_data/user_data.xlsx", "register_data", 2, 3)
        account_success_page = register_page.register_an_account(first_name, last_name,
                                                                 generate_email_with_current_time_stamp(), telephone,
                                                                 "123456", "123456", "no", "select")
        expected_message = "Your Account Has Been Created!"
        assert account_success_page.get_account_creation_success_message().__eq__(expected_message)

    @allure.severity(allure.severity_level.CRITICAL)
    def test_register_with_mandatory_fields_via_reading_data_from_json(self, open_register_page, read_register_data_from_json_file):
        logger.info("Test register with mandatory fields and reading data from json file")
        register_page = open_register_page
        data = read_register_data_from_json_file
        first_name = data["first_name"]
        last_name = data["last_name"]
        unique_email = generate_email_with_current_time_stamp()
        telephone = data["telephone"]
        password = data["password"]
        confirm_password = data["confirm_password"]
        no_select_news_letter = data["select_news_letter"]["no"]
        select_privacy_policy = data["select_privacy_policy"]["select"]
        account_success_page = register_page.register_an_account(first_name, last_name, unique_email, telephone,
                                                                 password, confirm_password, no_select_news_letter,
                                                                 select_privacy_policy)
        expected_message = "Your Account Has Been Created!"
        assert account_success_page.get_account_creation_success_message().__eq__(expected_message)

    @allure.severity(allure.severity_level.NORMAL)
    def test_register_with_all_fields(self, open_register_page, read_register_data_from_json_file):
        logger.info("Test register with all fields and reading data from json file")
        register_page = open_register_page
        data = read_register_data_from_json_file
        first_name = data["first_name"]
        last_name = data["last_name"]
        unique_email = generate_email_with_current_time_stamp()
        telephone = data["telephone"]
        password = data["password"]
        confirm_password = data["confirm_password"]
        yes_select_news_letter = data["select_news_letter"]["yes"]
        select_privacy_policy = data["select_privacy_policy"]["select"]
        account_success_page = register_page.register_an_account(first_name, last_name, unique_email, telephone,
                                                                 password, confirm_password, yes_select_news_letter,
                                                                 select_privacy_policy)
        expected_message = "Your Account Has Been Created!"
        assert account_success_page.get_account_creation_success_message().__eq__(expected_message)

    @allure.severity(allure.severity_level.NORMAL)
    def test_register_with_duplicated_email(self, open_register_page, read_register_data_from_json_file):
        logger.info("Test register with email already exists and reading data from json file")
        register_page = open_register_page
        data = read_register_data_from_json_file
        first_name = data["first_name"]
        last_name = data["last_name"]
        duplicated_email = data["email_already_exists"]
        telephone = data["telephone"]
        password = data["password"]
        confirm_password = data["confirm_password"]
        no_select_news_letter = data["select_news_letter"]["no"]
        select_privacy_policy = data["select_privacy_policy"]["select"]
        register_page.register_an_account(first_name, last_name, duplicated_email, telephone, password, confirm_password,
                                          no_select_news_letter, select_privacy_policy)
        expected_warning_message = "Warning: E-Mail Address is already registered!"
        assert register_page.get_invalid_register_warning_message().__contains__(expected_warning_message)

    @allure.severity(allure.severity_level.MINOR)
    def test_register_without_entering_any_fields(self, open_register_page, read_register_data_from_json_file):
        logger.info("Test register with empty fields and read the required no selection values "
                    "for checkboxes from json file")
        register_page = open_register_page
        data = read_register_data_from_json_file
        no_select_news_letter = data["select_news_letter"]["no"]
        no_select_privacy_policy = data["select_privacy_policy"]["no"]
        register_page.register_an_account("", "", "", "", "", "", no_select_news_letter, no_select_privacy_policy)
        expected_privacy_policy_warning_message = "Warning: You must agree to the Privacy Policy!"
        assert register_page.get_invalid_register_warning_message().__contains__(
            expected_privacy_policy_warning_message)
        expected_first_name_warning_message = "First Name must be between 1 and 32 characters!"
        assert register_page.get_first_name_warning_message().__contains__(expected_first_name_warning_message)

