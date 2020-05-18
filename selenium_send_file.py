from selenium import webdriver
import time
import math
import os 

link = 'http://suninjuly.github.io/file_input.html'
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

try:
    browser = webdriver.Chrome()
    browser.get(link)

    

    # Ваш код, который заполняет обязательные поля == 3 поля
    elements = browser.find_elements_by_xpath('//input[@type="text"]')
    for element in elements:
        element.send_keys("Мой ответ")

    input_element = browser.find_element_by_xpath('//input[@id="file"]')
    input_element.send_keys(file_path)


    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
