import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
 
try:
  browser = webdriver.Chrome()
  link = "http://suninjuly.github.io/explicit_wait2.html"
  browser.get(link)
  
  button1 = browser.find_element_by_css_selector("button#book")
  
  BookingPrice = WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h5#price"), "$100"))
  button1.click()
  
  text_to_convert = browser.find_element_by_css_selector("span#input_value")
  x= text_to_convert.text
  z = str(math.log(abs(12*math.sin(int(x)))))
  Field1 = browser.find_element_by_css_selector("input#answer")
  Field1.send_keys(z)

  button1 = browser.find_element_by_css_selector("button#solve")
  button1.click() 
  #Считаем формулу
  
finally:
  # ожидание чтобы визуально оценить результаты прохождения скрипта
  time.sleep(10)
  # закрываем браузер после всех манипуляций
  #browser.quit()

