from selenium import webdriver
import math
import os

try:
  browser = webdriver.Chrome()
  link = "http://suninjuly.github.io/alert_accept.html"
  browser.get(link)

  #Отправляем ответ
  button1 = browser.find_element_by_css_selector(".btn")
  button1.click()

  confirm = browser.switch_to.alert
  confirm.accept()

  #Получаем число для подсчёта
  text_to_convert = browser.find_element_by_css_selector("span#input_value")
  x= text_to_convert.text
  z = str(math.log(abs(12*math.sin(int(x)))))

  Field1 = browser.find_element_by_css_selector("input#answer")
  Field1.send_keys(z)

  button1 = browser.find_element_by_css_selector(".btn")
  button1.click()

  #Считаем формулу
  
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