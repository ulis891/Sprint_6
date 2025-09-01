import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()
