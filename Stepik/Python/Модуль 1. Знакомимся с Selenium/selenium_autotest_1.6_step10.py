from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_xpath("//label[text()='First name*']/following-sibling::input[@type='text']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath("//label[text()='Last name*']/following-sibling::input[@type='text']")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath("//label[text()='Email*']/following-sibling::input[@type='text']")
    input3.send_keys("test@test.ru")
    input4 = browser.find_element_by_xpath("//label[text()='Phone:']/following-sibling::input[@type='text']")
    input4.send_keys("+79393499487")
    input5 = browser.find_element_by_xpath("//label[text()='Address:']/following-sibling::input[@type='text']")
    input5.send_keys("Test adress Test")
    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()

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

# не забываем оставить пустую строку в конце файла
"""
By.ID – поиск по уникальному атрибуту id элемента;
By.CSS_SELECTOR – поиск элементов с помощью правил на основе CSS;
By.XPATH – поиск элементов с помощью языка запросов XPath;
By.NAME – поиск по атрибуту name элемента;
By.TAG_NAME – поиск по названию тега;
By.CLASS_NAME – поиск по атрибуту class элемента;
By.LINK_TEXT – поиск ссылки с указанным текстом. Текст ссылки должен быть точным совпадением;
By.PARTIAL_LINK_TEXT – поиск ссылки по частичному совпадению текста.
"""