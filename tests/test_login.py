import allure
import pytest
from utils.logger import logger
from pages.HomePage import HomePage
from utils import ExcelDataReader
from utils.utils import Utils


@pytest.mark.usefixtures("setup_and_teardown", "log_on_failure")
class TestLogin:
    not_registered_email = Utils.generate_email_with_current_time_stamp()
    logger.info("Read user_info from config.ini")
    user_email = Utils.read_configurations("user_info", "user_email")
    valid_user_password = Utils.read_configurations("user_info", "valid_user_password")
    invalid_user_password = Utils.read_configurations("user_info", "invalid_user_password")

    @pytest.fixture()
    def open_login_page(self):
        logger.info("This is open login page fixture")
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        yield login_page

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    @pytest.mark.sanity
    @pytest.mark.parametrize("user_email, password", ExcelDataReader.
                             get_data_from_excel("test_data/user_data.xlsx", "login_data"))
    def test_login_with_valid_credentials_by_reading_params_from_excel_file(self, user_email, password, open_login_page):
        logger.info("Test login with valid credentials from excel file")
        login_page = open_login_page
        account_page = login_page.login_to_application(user_email, password)
        assert account_page.check_edit_account_information_link_text_display_status()

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_login_with_valid_credentials_by_reading_data_from_config_file(self, open_login_page):
        logger.info("Test login with valid credentials by reading data from config file")
        login_page = open_login_page
        account_page = login_page.login_to_application(self.user_email, self.valid_user_password)
        assert account_page.check_edit_account_information_link_text_display_status()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_login_with_not_registered_email_and_valid_password(self, open_login_page):
        logger.info("Test login with not registered email and valid password")
        login_page = open_login_page
        login_page.login_to_application(self.not_registered_email, self.valid_user_password)
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.get_warning_message_text().__contains__(expected_warning_message)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_login_with_registered_email_and_invalid_password(self, open_login_page):
        logger.info("Test login with valid email and invalid password and values hard coded till now")
        login_page = open_login_page
        login_page.login_to_application(self.user_email, self.invalid_user_password)
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.get_warning_message_text().__contains__(expected_warning_message)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_login_without_entering_credentials(self, open_login_page):
        logger.info("Test login with empty email and password")
        login_page = open_login_page
        login_page.login_to_application("", "")
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.get_warning_message_text().__contains__(expected_warning_message)
