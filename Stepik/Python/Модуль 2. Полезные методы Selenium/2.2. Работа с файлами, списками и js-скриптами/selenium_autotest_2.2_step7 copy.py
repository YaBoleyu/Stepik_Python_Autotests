from selenium import webdriver
import math
try:


  browser = webdriver.Chrome()
  link = "http://suninjuly.github.io/execute_script.html"
  browser.get(link)
  #Получаем число для подсчёта
  text_to_convert = browser.find_element_by_css_selector("span#input_value")
  x= text_to_convert.text
  
  #Считаем формулу
  z = str(math.log(abs(12*math.sin(int(x)))))
  #Вписываем вычисления в поле для ответа
  input1 = browser.find_element_by_css_selector("input#answer")
  input1.send_keys(z)
  #Кликаем по робо-чекбоксам
  Checkbox1 = browser.find_elements_by_css_selector("label.form-check-label")
  for elem in Checkbox1:
    browser.execute_script("return arguments[0].scrollIntoView(true);", elem)
    if elem.is_displayed():
      elem.click()
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