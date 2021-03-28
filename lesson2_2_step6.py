from selenium import webdriver
import math
import time

try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    browser = webdriver.Chrome()
    browser.get("http://SunInJuly.github.io/execute_script.html")

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input)
    input.send_keys(y)

    option_check = browser.find_element_by_id("robotCheckbox")
    option_check.click()

    option_radio = browser.find_element_by_css_selector("[value='robots']")
    option_radio.click()

    option_but = browser.find_element_by_css_selector(".btn-primary")
    option_but.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()