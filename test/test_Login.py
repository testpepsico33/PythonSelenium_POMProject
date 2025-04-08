from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.AccountPage import AccountPage
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from test.BaseTest import BaseTest
from utilities import Excelutils


class TestLogin(BaseTest):

    @pytest.mark.parametrize("email_address,password",Excelutils.get_data_from_excel("C://Users//nimalkumar.j//PycharmProjects//HybridePythonSeleniumFramework//ExcelFiles//TutorialsNinja.xlsx","LoginTest"))
    def test_login_with_valid_credentials(self,email_address,password):
        home_page = HomePage(self.driver)

        login_page = home_page.navigate_to_login_page()

        account_page = login_page.login_to_application(email_address,password)
        assert account_page.edit_your_account_information_option_link_text

    def test_login_with_invalid_email_and_valid_password(self):
        home_page = HomePage(self.driver)

        login_page = home_page.navigate_to_login_page()

        login_page.login_to_application(self.generate_email_with_time_stamp(), "76@Kumar") #As its unsuccessful login not callin account page object
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."

        assert login_page.retrieve_warning_message().__eq__(expected_warning_message)

    def test_login_with_valid_email_and_invalid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()

        login_page.login_to_application("chittujs@yahoo.com","76@Kumar333333333")

        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__eq__(expected_warning_message)

    def test_login_without_entering_credentials(self):
        home_page = HomePage(self.driver)
        login_page=home_page.navigate_to_login_page()

        login_page.login_to_application("","")
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__eq__(expected_warning_message)


