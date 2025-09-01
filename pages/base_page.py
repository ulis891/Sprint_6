from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru/"

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def click_element(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        element.click()

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_element_to_be_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator),
            message=f"Element {locator} is not visible"
        )

    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator),
            message=f"Element {locator} is not clickable"
        )

    def wait_for_page_load(self, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete")

    def wait_for_new_tab(self, timeout=10):
        current_tabs_count = len(self.driver.window_handles)
        WebDriverWait(self.driver, timeout).until(
            lambda driver: len(driver.window_handles) > current_tabs_count
        )

    def switch_to_new_tab(self):
        original_tab = self.driver.current_window_handle
        for tab_handle in self.driver.window_handles:
            if tab_handle != original_tab:
                self.driver.switch_to.window(tab_handle)
                return tab_handle
        return None
