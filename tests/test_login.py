import allure
import pytest
from utils.logger import logger
from pages.HomePage import HomePage
from utils import ExcelDataReader, ReadConfigurations
from utils.utils import generate_email_with_current_time_stamp


@pytest.mark.usefixtures("setup_and_teardown", "log_on_failure")
class TestLogin:

    @pytest.fixture()
    def open_login_page(self):
        logger.info("This is open login page fixture")
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        yield login_page

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("user_email, password", ExcelDataReader.
                             get_data_from_excel("test_data/user_data.xlsx", "login_data"))
    def test_login_with_valid_credentials_by_reading_params_from_excel_file(self, user_email, password, open_login_page):
        logger.info("Test login with valid credentials from excel file")
        login_page = open_login_page
        account_page = login_page.login_to_application(user_email, password)
        assert account_page.check_edit_account_information_link_text_display_status()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_with_valid_credentials_by_reading_data_from_config_file(self, open_login_page):
        logger.info("Test login with valid credentials by reading data from config file")
        login_page = open_login_page
        user_email = ReadConfigurations.read_configurations("basic_info", "user_email")
        user_password = ReadConfigurations.read_configurations("basic_info", "valid_user_password")
        account_page = login_page.login_to_application(user_email, user_password)
        assert account_page.check_edit_account_information_link_text_display_status()

    @allure.severity(allure.severity_level.NORMAL)
    def test_login_with_invalid_email_and_valid_password(self, open_login_page):
        logger.info("Test login with invalid email and valid password")
        login_page = open_login_page
        not_registered_email = generate_email_with_current_time_stamp()
        user_password = ReadConfigurations.read_configurations("basic_info", "valid_user_password")
        login_page.login_to_application(not_registered_email, user_password)
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.get_warning_message_text().__contains__(expected_warning_message)

    @allure.severity(allure.severity_level.NORMAL)
    def test_login_with_valid_email_and_invalid_password(self, open_login_page):
        logger.info("Test login with valid email and invalid password and values hard coded till now")
        login_page = open_login_page
        user_email = ReadConfigurations.read_configurations("basic_info", "user_email")
        invalid_user_password = ReadConfigurations.read_configurations("basic_info", "invalid_user_password")
        login_page.login_to_application(user_email, invalid_user_password)
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.get_warning_message_text().__contains__(expected_warning_message)

    @allure.severity(allure.severity_level.NORMAL)
    def test_login_without_entering_credentials(self, open_login_page):
        logger.info("Test login with empty email and password")
        login_page = open_login_page
        login_page.login_to_application("", "")
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.get_warning_message_text().__contains__(expected_warning_message)
