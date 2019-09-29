link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add_to_basket(browser):
    browser.get(link)
    button1 = browser.find_element_by_class_name(
        "btn.btn-lg.btn-primary.btn-add-to-basket"
    )
    assert browser.find_element_by_class_name("btn-add-to-basket"), "Button is not available"
