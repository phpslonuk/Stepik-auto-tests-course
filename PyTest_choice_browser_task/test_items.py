import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_button(browser):
    browser.get(link)
    time.sleep(30)
    buy_button = browser.find_element_by_css_selector(
        ".btn-add-to-basket").text
    assert "" != buy_button
