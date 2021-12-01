from selenium import webdriver
import math
import os

try:
  current_dir = os.path.abspath(os.path.dirname(__file__))
  file_path = os.path.join(current_dir,"test.txt")


  browser = webdriver.Chrome()
  link = "http://suninjuly.github.io/file_input.html"
  browser.get(link)

  Field1 = browser.find_elements_by_css_selector(".form-control")
  for elem in Field1:
    if elem.is_displayed():
      elem.send_keys("Test")
  
  send_text_file = browser.find_element_by_css_selector("input#file")
  send_text_file.send_keys(file_path)




  #Отправляем ответ
  button1 = browser.find_element_by_css_selector(".btn")
  button1.click()

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