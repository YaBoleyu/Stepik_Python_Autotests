import time
from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    #link = "http://suninjuly.github.io/registration1.html"
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.form-control.first')
    input1.send_keys("Ivan")

    input2 = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.form-control.second')
    input2.send_keys("Popov")

    input3 = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.form-control.third')
    input3.send_keys("i.popov@gmail.com")
    # input4 = browser.find_element(By.CLASS_NAME, 'form-control.first')
    # input4.send_keys("+79999999999")
    # input5 = browser.find_element(By.CSS_SELECTOR, 'div.second_block>div.form-group.second_class>input')
    # input5.send_keys("Moscow")
    #button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
   #button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()