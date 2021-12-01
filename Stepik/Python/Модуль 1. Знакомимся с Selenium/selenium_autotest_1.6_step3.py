from selenium import webdriver
import time 

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath("//label[text()='First name:*']/following-sibling::input[@type='text']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath("//label[text()='Last name:*']/following-sibling::input[@type='text']")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath("//label[text()='City:*']/following-sibling::input[@type='text']")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_xpath("//label[text()='Country:*']/following-sibling::input[@type='text']")
    input4.send_keys("Russia")
    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
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