from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup_and_teardown")
class TestRegister:

    def test_register_with_mandatory_fields(self):

        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.XPATH,"//a[normalize-space()='Register']").click()
        self.driver.find_element(By.ID,"input-firstname").send_keys("Nirmal")
        self.driver.find_element(By.ID,"input-lastname").send_keys("CJ")
        self.driver.find_element(By.ID,"input-email").send_keys(self.generate_email_with_time_stamp())
        self.driver.find_element(By.ID,"input-telephone").send_keys("1234567890")
        self.driver.find_element(By.ID,"input-password").send_keys("12345")
        self.driver.find_element(By.ID,"input-confirm").send_keys("12345")
        self.driver.find_element(By.NAME,"agree").click()
        self.driver.find_element(By.XPATH,"//input[@type='submit']").click()
        expected_heading_text="Your Account Has Been Created!"
        assert self.driver.find_element(By.XPATH,"//div[@id='content']/h1").text.__eq__(expected_heading_text)


    def test_register_with_all_fields(self):

        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()
        self.driver.find_element(By.ID, "input-firstname").send_keys("Nirmal")
        self.driver.find_element(By.ID, "input-lastname").send_keys("CJ")
        self.driver.find_element(By.ID, "input-email").send_keys(self.generate_email_with_time_stamp())
        self.driver.find_element(By.ID, "input-telephone").send_keys("1234567890")
        self.driver.find_element(By.ID, "input-password").send_keys("12345")
        self.driver.find_element(By.XPATH,"//input[@name='newsletter'][@value='1']").click()
        self.driver.find_element(By.ID, "input-confirm").send_keys("12345")
        self.driver.find_element(By.NAME, "agree").click()
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        expected_heading_text = "Your Account Has Been Created!"
        assert self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__contains__((expected_heading_text))


    def test_register_with_duplicate_email(self):

        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()
        self.driver.find_element(By.ID, "input-firstname").send_keys("Nirmal")
        self.driver.find_element(By.ID, "input-lastname").send_keys("CJ")
        self.driver.find_element(By.ID, "input-email").send_keys("chittujs@yahoo.com")
        self.driver.find_element(By.ID, "input-telephone").send_keys("7904318630")
        self.driver.find_element(By.ID, "input-password").send_keys("76@Kumar")
        self.driver.find_element(By.XPATH, "//input[@name='newsletter'][@value='1']").click()
        self.driver.find_element(By.ID, "input-confirm").send_keys("12345")
        self.driver.find_element(By.NAME, "agree").click()
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        expected_warning_message = "Warning: E-Mail Address is already registered!"
        assert self.driver.find_element(By.XPATH, "//div[@id='account-register']/div[1]").text.__eq__(expected_warning_message)

    def generate_email_with_time_stamp(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "nirmalcjarav" + time_stamp + "@gmail.com"
    """
    def test_without_providing_any_field():
    
        driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()
        driver.find_element(By.XPATH, "//input[@type='submit']").click()
    """






