from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


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

    def wait_for_element_to_be_visible(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator),
            message=f"Element {locator} is not visible"
        )

    def wait_for_element_to_be_clickable(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator),
            message=f"Element {locator} is not clickable"
        )
