from selenium import webdriver
import math
z = ""
def calc(x):
  z = str(math.log(abs(12*math.sin(int(x)))))
  return z


try:


  link = "http://suninjuly.github.io/math.html"
  browser = webdriver.Chrome()
  browser.get(link)

  text_to_convert = browser.find_element_by_css_selector("span#input_value")
  
  x= text_to_convert.text
  print(x)

  z = str(math.log(abs(12*math.sin(int(x)))))

  input = browser.find_element_by_css_selector(".form-control")
  input.send_keys(z)

  checkbox1 = browser.find_elements_by_css_selector(".form-check-label")
  for elem in checkbox1:
    if elem.is_displayed():
        elem.click()
  
  button = browser.find_element_by_css_selector(".btn")
  button.click()

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