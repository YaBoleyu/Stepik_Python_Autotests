from selenium import webdriver
import math
z = ""
def calc(x):
  z = str(math.log(abs(12*math.sin(int(x)))))
  return z


try:


  link = "http://suninjuly.github.io/get_attribute.html"
  browser = webdriver.Chrome()
  browser.get(link)

  TreasureChest = browser.find_element_by_css_selector("img#treasure")
  
  x = TreasureChest.get_attribute("valuex")
  print(x)

  z = str(math.log(abs(12*math.sin(int(x)))))

  input = browser.find_element_by_css_selector("input#answer")
  input.send_keys(z)

  checkbox1 = browser.find_element_by_css_selector("input#robotCheckbox")
  checkbox1.click()

  radiobutton1 = browser.find_element_by_css_selector("input#robotsRule")
  radiobutton1.click()
  
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