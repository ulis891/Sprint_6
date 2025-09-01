from selenium.webdriver.common.by import By

from .base_page import BasePage


class OrderPage(BasePage):
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LASTNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION_OPTION = (By.XPATH, "//div[contains(@class, 'select-search__select')]//li")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DATE_PICKER = (By.CLASS_NAME, "react-datepicker")
    DATE_DAY = (By.CLASS_NAME, "react-datepicker__day")
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, "//div[contains(text(), 'Срок аренды')]")
    RENTAL_PERIOD_OPTION = (By.XPATH, "//div[contains(@class, 'Dropdown-option')]")
    COLOR_BLACK_CHECKBOX = (By.ID, "black")
    COLOR_GREY_CHECKBOX = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать' and contains(@class, 'Middle')]")

    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MODAL = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")
    STATUS_BUTTON = (By.XPATH, "//button[contains(text(), 'Посмотреть статус')]")

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

    def click_status_button(self):
        self.click_element(self.STATUS_BUTTON)

    def select_date_in_calendar(self, date):
        day = date.split(".")[0]
        self.find_element(self.DATE_INPUT).click()
        self.wait_for_element_to_be_visible(self.DATE_PICKER)
        days = self.find_elements(self.DATE_DAY)

        for day_element in days:
            if day_element.text == day and day_element.is_enabled():
                day_element.click()
                break

    def fill_rental_info(self, date, period, color, comment):
        # self.find_element(self.DATE_INPUT).send_keys(date)
        self.select_date_in_calendar(date)
        self.click_element(self.RENTAL_PERIOD_DROPDOWN)
        periods = self.find_elements(self.RENTAL_PERIOD_OPTION)
        for p in periods:
            if period in p.text:
                p.click()
                break

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
        success_element = self.find_element(self.SUCCESS_MODAL)
        return "Заказ оформлен" in success_element.text
