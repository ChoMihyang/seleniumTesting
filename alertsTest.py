from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

name = "Hello"

# ChromeDriver パス設定
service = Service(executable_path="/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()

# Switch to alert mode
alert = driver.switch_to.alert
alertText = alert.text

print(alertText)

assert name in alertText
alert.accept() # OK ボタンをクリック
# alert.dismiss()  # Cancel ボタンをクリック