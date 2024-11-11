from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


link = "http://suninjuly.github.io/explicit_wait2.html"

def culc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    WebDriverWait(browser,12).until(EC.element_to_be_clickable((By.ID, "book"))).click()

    x = browser.find_element(By.ID, "input_value").text
    y = culc(x)
    field = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", field)
    field.send_keys(y)
    browser.find_element(By.ID, "solve").click()
    


finally:
    time.sleep(15)
    browser.quit()