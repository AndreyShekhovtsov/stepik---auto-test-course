from selenium import webdriver
import time
import math


try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    button1 = browser.find_element_by_css_selector("button.trollface")
    button1.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input = browser.find_element_by_id("answer")
    input.send_keys(y)

    button2 = browser.find_element_by_css_selector("button.btn-primary")
    button2.click()

finally:
    time.sleep(10)
    browser.quit()