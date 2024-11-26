
# ПРОТЕСТИРОВАНО 26.11.24
# Значение переменной "2.3393096145457926"

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time 

link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    textArea = browser.find_element(By.ID, "answer")
    textArea.send_keys(str(math.log(int(time.time()))))

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()