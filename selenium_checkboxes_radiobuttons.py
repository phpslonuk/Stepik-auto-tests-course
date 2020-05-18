from selenium import webdriver
import time
import math

link = 'http://suninjuly.github.io/math.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element_by_xpath('//div/label/span[2]')

    x = x_element.text
    y = calc(x)

    answer = browser.find_element_by_xpath('//*[@id="answer"]')
    answer.send_keys(y)

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
