from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest



class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.XPATH, "//label[text()='First name*']/following-sibling::input[@type='text']")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH,"//label[text()='Last name*']/following-sibling::input[@type='text']")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH,"//label[text()='Email*']/following-sibling::input[@type='text']")
        input3.send_keys("test@test.ru")
        input4 = browser.find_element(By.XPATH,"//label[text()='Phone:']/following-sibling::input[@type='text']")
        input4.send_keys("+79393499487")
        input5 = browser.find_element(By.XPATH,"//label[text()='Address:']/following-sibling::input[@type='text']")
        input5.send_keys("Test adress Test")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR,"button.btn")
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
    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.XPATH, "//label[text()='First name*']/following-sibling::input[@type='text']")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH,"//label[text()='Last name*']/following-sibling::input[@type='text']")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH,"//label[text()='Email*']/following-sibling::input[@type='text']")
        input3.send_keys("test@test.ru")
        input4 = browser.find_element(By.XPATH,"//label[text()='Phone:']/following-sibling::input[@type='text']")
        input4.send_keys("+79393499487")
        input5 = browser.find_element(By.XPATH,"//label[text()='Address:']/following-sibling::input[@type='text']")
        input5.send_keys("Test adress Test")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR,"button.btn")
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


        
if __name__ == "__main__":
    unittest.main()


# не забываем оставить пустую строку в конце файла
"""
Возьмите тесты из шага — https://stepik.org/lesson/138920/step/11?unit=196194
Создайте новый файл
Создайте в нем класс с тестами, который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом
Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
Запустите получившиеся тесты из файла 
Просмотрите отчёт о запуске и найдите последнюю строчку 
Отправьте эту строчку в качестве ответа на это задание 
"""