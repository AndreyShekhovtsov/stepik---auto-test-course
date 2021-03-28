from selenium import webdriver
import time, random


random_string = "abcdefghijklmnopqrstuvwxyz"

try: 
    link = "http://suninjuly.github.io/registration1.html"
    #link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #required_fields = browser.find_elements_by_css_selector("input:required")
    #for field in required_fields:
    #    input_data = ''.join([random_string[random.randint(0,len(random_string) - 1)] for x in range(5)])
    #    field.send_keys(input_data)
    # Ваш код, который заполняет обязательные поля
    field1 = browser.find_element_by_css_selector("input.first:required")
    print("found 1st field: ", field1)
    input_data = ''.join([random_string[random.randint(0,len(random_string) - 1)] for x in range(5)])
    field1.send_keys(input_data)
    
    field2 = browser.find_element_by_css_selector("input.second:required")
    print("found 2nd field: ", field2)
    input_data = ''.join([random_string[random.randint(0,len(random_string) - 1)] for x in range(5)])
    field2.send_keys(input_data)
    
    field3 = browser.find_element_by_css_selector("input.third:required")
    print("found 3rd field: ", field3)
    input_data = ''.join([random_string[random.randint(0,len(random_string) - 1)] for x in range(5)])
    field3.send_keys(input_data)
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
#empty string
