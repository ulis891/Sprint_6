import pytest
import allure
from pages.main_page import MainPage
from data import ORDER_TEST_DATA


@allure.feature('Order Scooter')
@allure.story('Проверка процесса заказа самоката')
class TestOrderScooter:

    @allure.title('Успешный заказ самоката через {data[entry_point]} кнопку')
    @pytest.mark.parametrize('data', ORDER_TEST_DATA)
    def test_successful_order(self, driver, data):
        main_page = MainPage(driver)
        main_page.go_to_site()
        order_page = main_page.click_order_button(data["entry_point"])
        order_page.wait_for_page_load()
        order_page.fill_customer_info(data["customer"])
        order_page.click_next_button()
        order_page.fill_rental_info(data["rental"])
        order_page.click_order_button()
        order_page.confirm_order()
        assert order_page.is_order_successful(), "Заказ не был успешно оформлен"
        order_page.click_status_button()
        main_page.click_samokat_logo()
        main_page.wait_for_page_load()
        assert main_page.is_main_page(), "Не произошёл редирект на главную страницу Самоката"
        main_page.click_yandex_logo()
        main_page.switch_to_new_tab()
        main_page.wait_for_page_load()
        current_url = main_page.get_current_url()
        assert "dzen.ru" in current_url, f"Ожидался редирект на dzen.ru, получено: {current_url}"
