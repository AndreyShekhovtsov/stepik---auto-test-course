from selenium import webdriver
import time
import math

try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    button1 = browser.find_element_by_class_name("btn-primary")
    button1.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    time.sleep(1)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input = browser.find_element_by_id("answer")
    input.send_keys(y)

    button = browser.find_element_by_class_name("btn-primary")
    button.click()

finally:
    time.sleep(10)
    browser.quit()










