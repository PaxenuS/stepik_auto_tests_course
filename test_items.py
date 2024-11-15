import pytest
from selenium.webdriver.common.by import By
import time

def test_tusk(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.implicitly_wait(5)
    browser.get(link)
    add_product = browser.find_element(By.CSS_SELECTOR, "button.btn:nth-child(3)")
    assert add_product is not None, "Кнопка не обнаружена"