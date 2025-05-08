import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(executable_path="/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service)
# 暗黙的な待機
#   スクリプト全体に宣言する
#   アプリがページをロードするのにかかりそうな基本待機時間を適用する
driver.implicitly_wait(5) # 最大5秒を待機する。2秒で要素が表示されたら、次に進む

driver.get("https://rahulshettyacademy.com/seleniumPractise/")

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2) # 検索結果が表示されるまで待機、必ず指定した時間だけ待機する

# 暗黙的な待機にかからない。値のあるリストを取得するため（空きのリストのまま次に進んでしまうのを防ぐ）
products = driver.find_elements(By.XPATH, "//div[@class='products']/div")

for product in products:
    product.find_element(By.XPATH, "div/button").click() # chaining

driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

input("Press Enter to exit...")