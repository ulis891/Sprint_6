from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure
from .order_page import OrderPage


class MainPage(BasePage):
    ORDER_BUTTON_TOP = (By.XPATH, "//button[contains(text(), 'Заказать') and not(contains(@class, 'Middle'))]")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[contains(text(), 'Заказать') and contains(@class, 'Middle')]")

    FAQ_SECTION = (By.CSS_SELECTOR, "[data-accordion-component='Accordion']")
    FAQ_QUESTIONS = (By.CSS_SELECTOR, "[data-accordion-component='AccordionItem']")
    FAQ_QUESTION_BUTTONS = (By.CSS_SELECTOR, "[data-accordion-component='AccordionItemButton']")
    FAQ_ANSWER = (By.CSS_SELECTOR, "[data-accordion-component='Accordion'] p")

    SAMOKAT_LOGO = (By.XPATH, "//img[@alt='Scooter']/parent::a")
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']/parent::a")

    def __init__(self, driver):
        super().__init__(driver)

    def click_order_button(self, point):
        with allure.step(f"Кликнуть на кнопку заказа {point}"):
            if point == "top":
                self.click_element(self.ORDER_BUTTON_TOP)
            else:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                self.click_element(self.ORDER_BUTTON_BOTTOM)
            return OrderPage(self.driver)


    def scroll_to_bottom(self):
        with allure.step("Прокрутить до низа страницы"):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def click_samokat_logo(self):
        with allure.step("Кликнуть на логотип Самоката"):
            self.click_element(self.SAMOKAT_LOGO)
            self.wait_for_page_load()

    def click_yandex_logo(self):
        with allure.step("Кликнуть на логотип Яндекс"):
            self.click_element(self.YANDEX_LOGO)

    def is_main_page(self):
        with allure.step("Проверить, что находимся на главной странице"):
            return self.get_current_url() == self.base_url

    def get_faq_answer_text(self, index):
        with allure.step(f"Получить текст ответа на вопрос {index + 1}"):
            answer = self.find_elements(self.FAQ_ANSWER)
            return answer[index].text

    def click_faq_question(self, index):
        with allure.step(f"Кликнуть на вопрос {index + 1}"):
            answers = self.find_elements(self.FAQ_QUESTIONS)
            answers[index].click()
