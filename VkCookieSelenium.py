from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from vk import login, password
import pickle

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36")


driver = webdriver.Chrome(options=options)
url = "https://vk.com"

try:
    driver.get(url=url)
# Ввод логина
    login_input = driver.find_element(By.ID, "index_email")
    login_input.clear()
    login_input.send_keys(login)
    time.sleep(1)
# Отключение галочки (чекбокса) запоминания
    driver.find_element(By.CLASS_NAME, "VkIdCheckbox__checkboxOn").click()
    time.sleep(1)
    login_input.send_keys(Keys.ENTER)
    time.sleep(2)
# Ввод пароля
    password_input = driver.find_element(By.NAME, "password")
    password_input.clear()
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)
    time.sleep(5)

# Сохранить куки
    pickle.dump(driver.get_cookies(), open(f"{login}_cookies", "wb"))
    driver.get(url)
    time.sleep(2)

# Подгрузить куки из файла
    driver.get(url=url)
    for cookie in pickle.load(open(f"{login}_cookies", "rb")):
        driver.add_cookie(cookie)
    time.sleep(2)
    driver.refresh()
    time.sleep(3)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()