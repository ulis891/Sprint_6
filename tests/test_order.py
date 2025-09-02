import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import ORDER_TEST_DATA


@allure.feature('Order Scooter')
@allure.story('Проверка процесса заказа самоката')
class TestOrderScooter:

    # @allure.step('Открыть главную страницу')
    def open_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        return main_page

    def click_status_button(self, order_page):
        order_page.click_status_button()

    def click_order_button(self, main_page, driver, entry_point):
        main_page.click_order_button(entry_point)
        return OrderPage(driver)

    def fill_customer_info(self, order_page, customer_data):
        order_page.fill_customer_info(
            customer_data["name"],
            customer_data["lastname"],
            customer_data["address"],
            customer_data["metro_station"],
            customer_data["phone"]
        )
        order_page.click_next_button()

    def fill_rental_info(self, order_page, rental_data):
        order_page.fill_rental_info(
            rental_data["date"],
            rental_data["period"],
            rental_data["color"],
            rental_data["comment"]
        )
        order_page.click_order_button()

    def confirm_order(self, order_page):
        order_page.confirm_order()

    def verify_order_success(self, order_page):
        assert order_page.is_order_successful(), "Заказ не был успешно оформлен"

    def return_to_main_via_samokat_logo(self, order_page):
        main_page = MainPage(order_page.driver)
        main_page.click_samokat_logo()
        main_page.wait_for_page_load()
        assert main_page.is_main_page(), "Не произошёл редирект на главную страницу Самоката"
        return main_page

    def verify_yandex_redirect(self, main_page):
        main_page.click_yandex_logo()
        main_page.switch_to_new_tab()
        main_page.wait_for_page_load()
        current_url = main_page.get_current_url()
        assert "dzen.ru" in current_url, f"Ожидался редирект на dzen.ru, получено: {current_url}"

    @allure.title('Успешный заказ самоката через {data[entry_point]} кнопку')
    @pytest.mark.parametrize('data', ORDER_TEST_DATA)
    def test_successful_order(self, driver, data):
        main_page = self.open_main_page(driver)
        order_page = self.click_order_button(main_page, driver, data["entry_point"])
        self.fill_customer_info(order_page, data["customer"])
        self.fill_rental_info(order_page, data["rental"])
        self.confirm_order(order_page)
        self.verify_order_success(order_page)
        self.click_status_button(order_page)
        main_page = self.return_to_main_via_samokat_logo(order_page)
        self.verify_yandex_redirect(main_page)
