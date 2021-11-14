import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()
driver.maximize_window()
#Команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть что происходит в браузере
time.sleep(5)

driver.get("https://www.google.com")
time.sleep(5)

textarea = driver.find_element_by_class_name("gb_Pe")
driver.implicitly_wait(10)
ActionChains(driver).move_to_element(textarea).click(textarea).perform()
time.sleep(5)


#submit_button = driver.find_element_by_css_selector(".submit-submission")
#time.sleep(5)

driver.quit()