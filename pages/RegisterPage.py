from selenium.webdriver.common.by import By

from pages.AccountSuccessPage import AccountSuccessPage
from pages.BasePage import BasePage


class RegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    first_name_field_id="input-firstname"
    last_name_field_id="input-lastname"
    email_field_id="input-email"
    telephone_field_id="input-telephone"
    password_field_id="input-password"
    confirm_password_field_id="input-confirm"
    agree_field_name="agree"
    continue_button_xpath="//input[@type='submit']"
    email_already_registered_xpath="//div[@id='account-register']/div[1]"
    first_name_warning_message_xpath="//input[@id='input-firstname']/following-sibling::div"
    last_name_warning_message_xpath="//input[@id='input-lastname']/following-sibling::div"
    email_warning_message_xpath="//input[@id='input-email']/following-sibling::div"
    telephone_warning_message_xpath="//input[@id='input-telephone']/following-sibling::div"
    password_warning_message_xpath="//input[@id='input-password']/following-sibling::div"

    def enter_the_first_name_field(self,first_name_text):
        self.type_into_element(first_name_text,"first_name_field_id",self.first_name_field_id)
        #self.driver.find_element(By.ID,self.first_name_field_id).click()
        #self.driver.find_element(By.ID,self.first_name_field_id).clear()
        #self.driver.find_element(By.ID,self.first_name_field_id).send_keys(first_name_text)
    def enter_the_last_name_field(self,last_name_text):
        self.type_into_element(last_name_text,"last_name_field_id",self.last_name_field_id)
        #self.driver.find_element(By.ID,self.last_name_field_id).click()
        #self.driver.find_element(By.ID, self.last_name_field_id).clear()
        #self.driver.find_element(By.ID, self.last_name_field_id).send_keys(last_name_text)

    def enter_the_email(self,emailid_text):
        self.type_into_element(emailid_text,"email_field_id",self.email_field_id)
        #self.driver.find_element(By.ID,self.email_field_id).click()
        #self.driver.find_element(By.ID,self.email_field_id).clear()
        #self.driver.find_element(By.ID,self.email_field_id).send_keys(emailid_text)

    def enter_the_telephone(self,telephone_number):
        self.type_into_element(telephone_number,"telephone_field_id",self.telephone_field_id)
        #self.driver.find_element(By.ID,self.telephone_field_id).click()
        #self.driver.find_element(By.ID,self.telephone_field_id).clear()
        #self.driver.find_element(By.ID, self.telephone_field_id).send_keys(telephone_number)

    def enter_the_password(self,password_text):
        self.type_into_element(password_text,"password_field_id",self.password_field_id)
        #self.driver.find_element(By.ID,self.password_field_id).click()
        #self.driver.find_element(By.ID,self.password_field_id).clear()
        #self.driver.find_element(By.ID,self.password_field_id).send_keys(password_text)

    def enter_the_confirm_password(self,confirm_password_text):
        self.type_into_element(confirm_password_text,"confirm_password_field_id",self.confirm_password_field_id)
        #self.driver.find_element(By.ID, self.confirm_password_field_id).click()
        #self.driver.find_element(By.ID, self.confirm_password_field_id).clear()
        #self.driver.find_element(By.ID, self.confirm_password_field_id).send_keys(confirm_password_text)

    def select_agree_checkbox_field(self):
        self.element_click("agree_field_name",self.agree_field_name)
        #self.driver.find_element(By.NAME,self.agree_field_name).click()

    def click_on_continue_button(self):
        self.element_click("continue_button_xpath",self.continue_button_xpath)
        #self.driver.find_element(By.XPATH,self.continue_button_xpath).click()
        return AccountSuccessPage(self.driver)
    # Above all methods bring into a single method
    def register_an_account(self,first_name_text,last_name_text,emailid_text,
                            telephone_number,password_text,confirm_password_text,Privacy_Policy):

        self.enter_the_first_name_field(first_name_text)
        self.enter_the_last_name_field(last_name_text)
        self.enter_the_email(emailid_text)
        self.enter_the_telephone(telephone_number)
        self.enter_the_password(password_text)
        self.enter_the_confirm_password(confirm_password_text)
        if Privacy_Policy.__eq__("select"):
            self.select_agree_checkbox_field()
        return self.click_on_continue_button()


    def retrieve_email_already_registered_message(self):
        return self.retrive_element_text("email_already_registered_xpath",self.email_already_registered_xpath)
        #return self.driver.find_element(By.XPATH,self.email_already_registered_xpath).text

    def retrieve_first_name_warning_message(self):
        return self.retrive_element_text("first_name_warning_message_xpath",self.first_name_warning_message_xpath)
        #return self.driver.find_element(By.XPATH,self.first_name_warning_message_xpath).text

    def retrieve_last_name_warning_message(self):
        return self.retrive_element_text("last_name_warning_message_xpath",self.last_name_warning_message_xpath)
        #return self.driver.find_element(By.XPATH,self.last_name_warning_message_xpath).text

    def retrieve_email_warning_message(self):
        return self.retrive_element_text("email_warning_message_xpath",self.email_warning_message_xpath)
        #return self.driver.find_element(By.XPATH,self.email_warning_message_xpath).text

    def retrieve_telephone_warning_message(self):
        return self.retrive_element_text("telephone_warning_message_xpath",self.telephone_warning_message_xpath)
        #return self.driver.find_element(By.XPATH,self.telephone_warning_message_xpath).text

    def retrieve_password_warning_message(self):
        return self.retrive_element_text("password_warning_message_xpath",self.password_warning_message_xpath)
        #return self.driver.find_element(By.XPATH,self.password_warning_message_xpath).text

    def verify_all_warnings(self,expected_first_name_warning_message,expected_last_name_warning_message,expected_email_warning_message,expected_telephone_warning_message,expected_password_warning_message):
        actual_first_name_warning_message=self.retrieve_first_name_warning_message()
        actual_last_name_warning_message=self.retrieve_last_name_warning_message()
        actual_email_warning_message=self.retrieve_email_warning_message()
        actual_telephone_warning_message=self.retrieve_telephone_warning_message()
        actual_password_warning_message=self.retrieve_password_warning_message()

        status= False

        if expected_first_name_warning_message.__eq__(actual_first_name_warning_message):
            if expected_last_name_warning_message.__eq__(actual_last_name_warning_message):
                if(expected_email_warning_message).__eq__(actual_email_warning_message):
                    if(expected_telephone_warning_message).__eq__(actual_telephone_warning_message):
                        if(expected_password_warning_message).__eq__(actual_password_warning_message):
                            status= True
        return status




