from selenium.webdriver.common.by import By

from .base_page import BasePage


class DzenPage(BasePage):
    DZEN_LOGO = (By.CSS_SELECTOR, "[aria-label='Логотип Бренда']")
    DZEN_SEARCH_INPUT = (By.XPATH, "//form/input[@aria-label='Запрос']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_dzen_loaded(self):
        try:
            self.wait_for_element_to_be_visible(self.DZEN_LOGO)
            self.wait_for_element_to_be_visible(self.DZEN_SEARCH_INPUT)
            return True
        except:
            return False
