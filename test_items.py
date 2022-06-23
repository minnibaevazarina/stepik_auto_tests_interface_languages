import time
from selenium.webdriver.common.by import By

def test_button_add_to_cart_exist(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    button = browser.find_element(By.XPATH, "//button[contains(@class, 'basket')]")
    assert button, "button is missing"
