from datetime import datetime

import pytest
from gevent.resolver import thread
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.AccountSuccessPage import AccountSuccessPage
from pages.HomePage import HomePage
from pages.RegisterPage import RegisterPage
from test.BaseTest import BaseTest


class TestRegister(BaseTest):

    def test_register_with_mandatory_fields(self):
        home_page = HomePage(self.driver)
        register_page=home_page.navigate_to_register_page()

        account_success_page=register_page.register_an_account("Nirmal Kumar","CJ",self.generate_email_with_time_stamp(),"1234567890","12345","12345","select")

        expected_heading_text = "Your Account Has Been Created!"
        assert account_success_page.retrieve_account_creation_message().__eq__(expected_heading_text)

    def test_register_with_all_fields(self):
        home_page = HomePage(self.driver)
        register_page=home_page.navigate_to_register_page()

        account_success_page = register_page.register_an_account("Nirmal Kumar", "CJ",
                                                                 self.generate_email_with_time_stamp(), "1234567890",
                                                                 "12345", "12345", "select")

        expected_heading_text = "Your Account Has Been Created!"
        assert account_success_page.retrieve_account_creation_message().__eq__(expected_heading_text)

    def test_register_with_duplicate_email(self):
        home_page = HomePage(self.driver)
        register_page=home_page.navigate_to_register_page()

        register_page.register_an_account("Nirmal Kumar","CJ","chittujs@yahoo.com","1234567890","12345","12345","select")

        expected_warning_message = "Warning: E-Mail Address is already registered!"
        assert register_page.retrieve_email_already_registered_message().__eq__(expected_warning_message)

    def test_register_with_not_entering_values(self):
        home_page = HomePage(self.driver)
        register_page=home_page.navigate_to_register_page()

        register_page.register_an_account("","","","","","","no")
        assert register_page.verify_all_warnings("First Name must be between 1 and 32 characters!","Last Name must be "
                                                                                                   "between 1 and 32 "
                                                                                                   "characters!",
                                                 "E-Mail Address does not appear to be valid!","Telephone must be "
                                                                                               "between 3 and 32 "
                                                                                               "characters!",
                                                 "Password must be between 4 and 20 characters!")

"""
    def generate_email_with_time_stamp(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "nirmalcjarav" + time_stamp + "@gmail.com"

   
    def test_without_providing_any_field():
    
        driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()
        driver.find_element(By.XPATH, "//input[@type='submit']").click()
    """
