# 請先執行自動登入獲取cookie.py獲取cookies再執行py檔
# 嘗試讀取 cookies
try:
    with open('cookies.txt', 'r') as f:
        cookies = f.readlines()
    for cookie in cookies:
        driver.add_cookie(eval(cookie))
except FileNotFoundError:
   print("沒有cookies儲存")
