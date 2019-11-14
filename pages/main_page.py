from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainPage(Page):
    SEARCH_INPUT = (By.ID, "twotabsearchtextbox")
    SEARCH_ICON = (By.CSS_SELECTOR, "input.nav-input[type='submit']")

    def search_for_keyword(self, text):
        self.input_text(text, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_ICON)
