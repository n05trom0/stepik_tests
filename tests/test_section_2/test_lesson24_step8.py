
# ПРОТЕСТИРОВАНО 26.11.24

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Ожидаем, пока цена станет $100
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    
    # Клик по кнопке "Book"
    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    # Вычисляем значение
    x = int(browser.find_element(By.ID, "input_value").text)
    y = str(math.log(abs(12 * math.sin(x))))

    # Вводим ответ
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    # Ожидаем кликабельности кнопки и кликаем
    submit_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "solve"))
    )
    submit_button.click()

finally:
    # Пауза для копирования результата
    time.sleep(30)
    browser.quit()
