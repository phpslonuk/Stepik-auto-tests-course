from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

link = 'http://SunInJuly.github.io/execute_script.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element_by_xpath('//span[@id="input_value"]')
    
    x = x_element.text
    print(x)
    res = calc(x)
    print(res)
    
    answer = browser.find_element_by_xpath('//input[@id="answer"]')
    answer.send_keys(res)

    browser.execute_script("window.scrollBy(0, 100);")

    robot_check = browser.find_element_by_xpath('//*[@id="robotCheckbox"]')
    robot_check.click()

    robot_rule = browser.find_element_by_xpath('//input[@id="robotsRule"]')
    robot_rule.click()

    button = browser.find_element_by_xpath('//button')
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
