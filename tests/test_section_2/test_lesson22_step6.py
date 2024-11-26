
# ПРОТЕСТИРОВАНО 26.11.24

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "https://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Найти значение x и вычислить результат
    num1 = browser.find_element(By.ID, "input_value").text
    result = calc(num1)

    # Ввести результат в поле
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(result)

    # Отметить checkbox
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    # Выбрать radiobutton
    radio = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)    
    radio.click()

    # Скроллинг до кнопки
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    # Клик по кнопке
    button.click()

finally:
    # Пауза для проверки
    time.sleep(30)
    # Закрыть браузер
    browser.quit()