from selenium import webdriver
import math

try:


  link = "http://suninjuly.github.io/selects1.html"
  browser = webdriver.Chrome()
  browser.get(link)
  
  Number_1 = browser.find_element_by_css_selector("span#num1")
  Number_2 = browser.find_element_by_css_selector("span#num2")
  
  x = int(Number_1.text) + int(Number_2.text)
  x =str(x)
  print(x)


  dropdown = browser.find_element_by_css_selector("select#dropdown")
  dropdown.click()

  summ = browser.find_element_by_css_selector("option[value='%s']"%(x))
  summ.click()
  dropdown.click()

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