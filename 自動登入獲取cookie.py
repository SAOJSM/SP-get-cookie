from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import requests
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 設定 User-Agent
# 此步驟避免被判斷為機器人爬蟲程式，設置完成不會出現拼圖驗證
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/2.0'
}

# 初始化 WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 訪問蝦皮購物網站
driver.get('https://shopee.tw/buyer/login')

# 輸入帳號密碼
# 等待用戶名輸入框出現
username_input = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.NAME, "loginKey"))
)

# your_username修改為用戶名
username_input.send_keys("your_username")

# 等待密碼輸入框出現
password_input = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.NAME, "password"))
)

# your_password修改為密碼
password_input.send_keys("your_password")

# 完成上面步驟請手動按登入

# 等待頁面加載
# 此行程式用於完成新環境登入訊驗證碼的步驟
time.sleep(30)

# 獲取 cookies
cookies = driver.get_cookies()

# 儲存 cookies
with open('cookies.txt', 'w') as f:
    for cookie in cookies:
        f.write(str(cookie) + '\n')

# 關閉 WebDriver
driver.quit()
