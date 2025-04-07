from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class SearchPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    valid_hp_product_link_text="HP LP3065"
    no_product_message_xpath="(//p[contains(text(),'There is no product that matches the search criter')])[1]"

    def display_status_of_valid_product(self):
        return self.get_element("valid_hp_product_link_text",self.valid_hp_product_link_text)
        # return self.driver.find_element(By.LINK_TEXT,self.valid_hp_product_link_text).is_displayed()
        #return, the values to pass back from the function

    def retrieve_no_product_message(self):
        return self.retrive_element_text("no_product_message_xpath",self.no_product_message_xpath)
        #return self.driver.find_element(By.XPATH,self.no_product_message_xpath).text