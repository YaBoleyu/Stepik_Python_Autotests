import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"

#Фикстура для прохождения кейсов в одном и том же браузере
@pytest.fixture(scope="class")
def browser():
    print("start browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("quit browser..")
    browser.quit()


class TestMainPage1():

    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        print("start test1")
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")
        print("finish test1")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("start test2")
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
        print("finish test2")