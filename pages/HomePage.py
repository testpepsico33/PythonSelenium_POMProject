from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from pages.LoginPage import LoginPage
from pages.RegisterPage import RegisterPage
from pages.SearchPage import SearchPage


class HomePage(BasePage):
    def __init__(self, driver):  # driver is passed to launch the browser
        super().__init__(driver)

    search_box_field_name = "search"
    search_button_xpath = "//button[contains(@class,'btn-default')]"
    my_account_drop_menu_xpath = "//span[text()='My Account']"
    login_option_link_text = "Login"
    register_option_link_text = "Register"

    def enter_product_into_search_box_field(self, product_name):
        self.type_into_element(product_name,"search_box_field_name",self.search_box_field_name)

    def click_on_search_button(self):
        self.element_click("search_button_xpath",self.search_button_xpath)
        #This locatore stored in basepage under a method and calling the method
        #self.driver.find_element(By.XPATH, self.search_button_xpath).click()
        return SearchPage(self.driver)

    def click_on_my_account_drop_menu(self):
        self.element_click("my_account_drop_menu_xpath",self.my_account_drop_menu_xpath)
        #This locatore stored in basepage under a method and calling the method
        #self.driver.find_element(By.XPATH, self.my_account_drop_menu_xpath).click()
        return SearchPage(self.driver)

    def select_login_option(self):
        self.element_click("login_option_link_text",self.login_option_link_text)
        #This locatore stored in basepage under a method and calling the method
        #self.driver.find_element(By.LINK_TEXT, self.login_option_link_text).click()
        return LoginPage(self.driver)
    #Converting into single method
    def navigate_to_login_page(self):
        self.click_on_my_account_drop_menu()
        return self.select_login_option() # Already select_login_option method returning LoginPage the same will be return by navigate_to_login_page method

    def select_register_option(self):
        self.element_click("register_option_link_text",self.register_option_link_text)
        #self.driver.find_element(By.LINK_TEXT, self.register_option_link_text).click()
        return RegisterPage(self.driver)

    def navigate_to_register_page(self):
        self.click_on_my_account_drop_menu()
        return self.select_register_option()

    # Methods integration to reduce code
    def search_for_a_product(self, product_name):
        self.enter_product_into_search_box_field(product_name)
        return self.click_on_search_button()

