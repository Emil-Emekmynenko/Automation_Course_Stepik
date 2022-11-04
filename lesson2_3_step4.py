from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # нажимаю модальную кнопку
    button = browser.find_element(By.CLASS_NAME, "btn-primary")
    button.click()
    # выбираю алерт и закрываю его
    confirm = browser.switch_to.alert
    confirm.accept()
    # расчёт формулы
    x_element = browser.find_element(By.XPATH, "//*[@id='input_value']")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    input1.send_keys(y)
    # button
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    # Вытащить текст из алерта
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

