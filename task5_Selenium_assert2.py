from selenium import webdriver
import time

try:
    link_good = "http://suninjuly.github.io/registration1.html"
    link_error = 'http://suninjuly.github.io/registration2.html'
    browser = webdriver.Chrome()
    browser.get(link_error)

    # Ваш код, который заполняет обязательные поля == 3 поля
    req_elements = browser.find_elements_by_tag_name('input[required]')
    elements = browser.find_elements_by_tag_name('input')
    if len(req_elements) == 3:
        for element in elements:
            element.send_keys("Мой ответ")
    else:
        # Кто знаєт как кидать ошибку в selenium
        input2 = browser.find_element_by_name('--*O_o*--')

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
