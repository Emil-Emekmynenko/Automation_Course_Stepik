from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.XPATH, "//*[@id='input_value']")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    input1.send_keys(y)
    #checkbox
    option1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    option1.click()
    #radiocnopka
    option2 = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    option2.click()
    #button
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()