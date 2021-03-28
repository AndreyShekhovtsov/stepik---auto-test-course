from selenium import webdriver
import math
import time
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects2.html")

    # находим элемент, содержащий текст
    x1 = browser.find_element_by_id("num1").text
    x2 = browser.find_element_by_id("num2").text

    y = str(int(x1) + int(x2))

    select = Select(browser.find_element_by_tag_name("select"))
    x = select.select_by_visible_text(y)

    option_but = browser.find_element_by_css_selector(".btn-default")
    option_but.click()

finally:
    time.sleep(10)
    browser.quit()
