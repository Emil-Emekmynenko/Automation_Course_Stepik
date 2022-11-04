from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    a = browser.find_element(By.ID,"num1").text # перевод элемента в текст
    b = browser.find_element(By.ID,"num2").text # перевод элемента в текст
    result = int(a)+int(b)
    # ищим элемент в выпадающем списке
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(result))
    # ищим кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()