import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.HomePage import HomePage
from pages.SearchPage import SearchPage
from test.BaseTest import BaseTest


class TestSearch(BaseTest):

    def test_search_for_valid_product(self):
        home_page=HomePage(self.driver)
        search_page=home_page.search_for_a_product("HP")
        assert search_page.display_status_of_valid_product()


    def test_search_for_invalid_product(self):
        home_page = HomePage(self.driver)
        search_page=home_page.search_for_a_product("Honda")
        expected_text="There is no product that matches the search criteria."
        assert search_page.retrieve_no_product_message().__eq__(expected_text)


    def test_search_without_entering_any_product_name(self):
        home_page = HomePage(self.driver)
        search_page=home_page.search_for_a_product("")
        expected_text = "There is no product that matches the search criteria.ABC"
        assert search_page.retrieve_no_product_message().__eq__(expected_text)




