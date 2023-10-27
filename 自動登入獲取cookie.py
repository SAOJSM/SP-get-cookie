# 使用requests和selenium模組，需要安裝chromedriver
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 設定登入的帳號和密碼
username = "your_username"
password = "your_password"

# 建立一個session物件，用來保存cookie
session = requests.Session()

# 建立一個webdriver物件，用來控制瀏覽器
driver = webdriver.Chrome()

# 打開蝦皮購物的登入頁面
url="https://shopee.tw/buyer/login"
driver.get(url)

# 找到帳號和密碼的輸入框，並輸入相應的值
username_input = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.NAME, "loginKey"))
)
username_input.send_keys(username)
password_input = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.NAME, "password"))
)
password_input.send_keys(password)
waittime = WebDriverWait(driver, 30)

# 等待登錄成功後的頁面出現
waittime = WebDriverWait(driver, 30)
driver.get(url)
cookies = driver.get_cookies()

# 將cookie加入session物件中
for cookie in cookies:
    session.cookies.set(cookie["name"], cookie["value"])

# 關閉瀏覽器
driver.quit()