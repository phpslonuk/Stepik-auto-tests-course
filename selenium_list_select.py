from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

link = 'http://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x, y):
        return str(x + y)

    x_element = browser.find_element_by_xpath('//span[@id="num1"]')
    y_element = browser.find_element_by_xpath('//span[@id="num2"]')

    x = int(x_element.text)
    y = int(y_element.text)
    answer = calc(x, y)

    select = Select(browser.find_element_by_xpath('//select[@id="dropdown"]'))
    select.select_by_value(answer)

    button = browser.find_element_by_xpath('//button')
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
