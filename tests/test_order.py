import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from tests.data import ORDER_TEST_DATA


@allure.feature('Order Scooter')
@allure.story('Проверка процесса заказа самоката')
class TestOrderScooter:

    @allure.step('Открыть главную страницу')
    def open_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        return main_page

    @allure.step('Кликнуть на кнопку заказа ({entry_point})')
    def click_order_button(self, main_page, driver, entry_point):
        if entry_point == "top":
            main_page.click_order_button_top()
        else:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            main_page.click_order_button_bottom()
        return OrderPage(driver)

    @allure.step('Заполнить информацию о клиенте')
    def fill_customer_info(self, order_page, customer_data):
        order_page.fill_customer_info(
            customer_data["name"],
            customer_data["lastname"],
            customer_data["address"],
            customer_data["metro_station"],
            customer_data["phone"]
        )
        order_page.click_next_button()

    @allure.step('Заполнить информацию об аренде')
    def fill_rental_info(self, order_page, rental_data):
        order_page.fill_rental_info(
            rental_data["date"],
            rental_data["period"],
            rental_data["color"],
            rental_data["comment"]
        )
        order_page.click_order_button()

    @allure.step('Подтвердить заказ')
    def confirm_order(self, order_page):
        order_page.confirm_order()

    @allure.step('Проверить успешность оформления заказа')
    def verify_order_success(self, order_page):
        assert order_page.is_order_successful(), "Заказ не был успешно оформлен"

    @allure.title('Успешный заказ самоката через {data[entry_point]} кнопку')
    @pytest.mark.parametrize('data', ORDER_TEST_DATA)
    def test_successful_order(self, driver, data):
        main_page = self.open_main_page(driver)
        order_page = self.click_order_button(main_page, driver, data["entry_point"])
        self.fill_customer_info(order_page, data["customer"])
        self.fill_rental_info(order_page, data["rental"])
        self.confirm_order(order_page)
        self.verify_order_success(order_page)
