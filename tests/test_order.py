import pytest
import allure
from pages.main_page import MainPage


@allure.feature('Order Scooter')
@allure.story('Проверка процесса заказа самоката')
class TestOrderScooter:

    @allure.step('Открыть главную страницу')
    def open_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        return main_page

    @allure.step('Кликнуть на кнопку заказа')
    def click_order_button(self, main_page, driver):
        main_page.click_order_button_top()

    def test_test(self, driver):
        main_page = self.open_main_page(driver)
        self.click_order_button(main_page, driver)
