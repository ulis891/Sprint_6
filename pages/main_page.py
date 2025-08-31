from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    ORDER_BUTTON_TOP = (By.XPATH, "//button[contains(text(), 'Заказать') and not(contains(@class, 'Middle'))]")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[contains(text(), 'Заказать') and contains(@class, 'Middle')]")

    FAQ_SECTION = (By.CSS_SELECTOR, "[data-accordion-component='Accordion']")
    FAQ_QUESTIONS = (By.CSS_SELECTOR, "[data-accordion-component='AccordionItem']")
    FAQ_QUESTION_BUTTONS = (By.CSS_SELECTOR, "[data-accordion-component='AccordionItemButton']")
    FAQ_ANSWERS = (By.CSS_SELECTOR, "[data-accordion-component='AccordionItemPanel']")

    SAMOKAT_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

    def __init__(self, driver):
        super().__init__(driver)

    def click_order_button_top(self):
        self.click_element(self.ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        self.click_element(self.ORDER_BUTTON_BOTTOM)

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def click_samokat_logo(self):
        self.click_element(self.SAMOKAT_LOGO)
        self.wait_for_page_load()

    def click_yandex_logo(self):
        self.click_element(self.YANDEX_LOGO)

    def is_main_page(self):
        return self.get_current_url() == self.base_url

    def get_faq_answer_text(self, index):
        answers = self.find_elements(self.FAQ_ANSWERS)
        return answers[index].text



