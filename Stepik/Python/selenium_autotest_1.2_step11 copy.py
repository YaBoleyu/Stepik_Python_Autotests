import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

#Команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть что происходит в браузере
time.sleep(5)

driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(5)

textarea = driver.find_element_by_css_selector(".textarea")

textarea.send_keys("get()")
time.sleep(5)

submit_button = driver.find_element_by_css_selector(".submit-submission")
time.sleep(5)

driver.quit()