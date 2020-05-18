from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

link = 'http://suninjuly.github.io/alert_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    button = browser.find_element_by_xpath('//button')
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()
    
    time.sleep(1)
    x_element = browser.find_element_by_xpath('//span[@id="input_value"]')
    x = x_element.text
    res = calc(x)

    answer = browser.find_element_by_xpath('//input[@id="answer"]')
    answer.send_keys(res)


    button = browser.find_element_by_xpath('//button')
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
