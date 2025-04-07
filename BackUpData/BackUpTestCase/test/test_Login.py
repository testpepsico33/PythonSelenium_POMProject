from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By




@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:

    def test_login_with_valid_credentials(self):
        self.driver.find_element(By.XPATH,"//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT,"Login").click()
        self.driver.find_element(By.ID,"input-email").send_keys("chittujs@yahoo.com")
        self.driver.find_element(By.ID,"input-password").send_keys("76@Kumar")
        self.driver.find_element(By.XPATH,"//input[contains(@class,'btn btn-primary')]").click()
        assert self.driver.find_element(By.LINK_TEXT,"Edit your account information").is_displayed()


    def test_login_with_invalid_email_and_valid_password(self):

        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.ID, "input-email").send_keys(self.generate_email_with_time_stamp())
        self.driver.find_element(By.ID, "input-password").send_keys("76@Kumar")
        self.driver.find_element(By.XPATH,"//input[contains(@class,'btn btn-primary')]").click()
        expected_warning_message="Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH,"//div[@id='account-login']/div[1]").text.__contains__(expected_warning_message)


    def test_login_with_valid_email_and_invalid_password(self):

        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.ID, "input-email").send_keys("chittujs@yahoo.com")
        self.driver.find_element(By.ID, "input-password").send_keys("76@Kumarnirmal")
        self.driver.find_element(By.XPATH, "//input[contains(@class,'btn btn-primary')]").click()
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text.__contains__(
            expected_warning_message)


    def test_login_without_entering_credentials(self):

        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.ID, "input-email").send_keys("")
        self.driver.find_element(By.ID, "input-password").send_keys("")
        self.driver.find_element(By.XPATH, "//input[contains(@class,'btn btn-primary')]").click()
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text.__contains__(
            expected_warning_message)



    def generate_email_with_time_stamp(self):
        time_stamp=datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "nirmalcjarav"+time_stamp+"@gmail.com"
