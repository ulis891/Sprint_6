from selenium.webdriver.common.by import By
from .base_page import BasePage


class OrderPage(BasePage):
    # Улучшенные локаторы для формы заказа
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LASTNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION_OPTION = (By.XPATH, "//div[contains(@class, 'select-search__select')]//li")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Локаторы для второй части формы
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, "//div[contains(text(), 'Срок аренды')]")
    RENTAL_PERIOD_OPTION = (By.XPATH, "//div[contains(@class, 'Dropdown-option')]")
    COLOR_BLACK_CHECKBOX = (By.ID, "black")
    COLOR_GREY_CHECKBOX = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать' and contains(@class, 'Middle')]")

    # Локаторы для подтверждения заказа
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MODAL = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")

    def __init__(self, driver):
        super().__init__(driver)

    def fill_customer_info(self, name, lastname, address, metro_station, phone):
        self.find_element(self.NAME_INPUT).send_keys(name)
        self.find_element(self.LASTNAME_INPUT).send_keys(lastname)
        self.find_element(self.ADDRESS_INPUT).send_keys(address)

        self.find_element(self.METRO_STATION_INPUT).click()
        stations = self.find_elements(self.METRO_STATION_OPTION)
        for station in stations:
            if metro_station in station.text:
                station.click()
                break

        self.find_element(self.PHONE_INPUT).send_keys(phone)

    def click_next_button(self):
        self.click_element(self.NEXT_BUTTON)

    def fill_rental_info(self, date, period, color, comment):
        self.find_element(self.DATE_INPUT).send_keys(date)
        self.click_element(self.RENTAL_PERIOD_DROPDOWN)
        periods = self.find_elements(self.RENTAL_PERIOD_OPTION)
        for p in periods:
            if period in p.text:
                p.click()
                break

        # Выбор цвета
        if color == "black":
            self.click_element(self.COLOR_BLACK_CHECKBOX)
        elif color == "grey":
            self.click_element(self.COLOR_GREY_CHECKBOX)

        if comment:
            self.find_element(self.COMMENT_INPUT).send_keys(comment)

    def click_order_button(self):
        self.click_element(self.ORDER_BUTTON)

    def confirm_order(self):
        self.click_element(self.CONFIRM_ORDER_BUTTON)

    def is_order_successful(self):
        try:
            success_element = self.find_element(self.SUCCESS_MODAL, time=10)
            return "Заказ оформлен" in success_element.text
        except:
            return False
