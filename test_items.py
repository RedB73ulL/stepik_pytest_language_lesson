from selenium.webdriver.common.by import By
import time

def test_function_find_button(browser):
    link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    browser.get(link)
    browser.implicitly_wait(5)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")

    assert button > 0, "No button"

    time.sleep(10)
