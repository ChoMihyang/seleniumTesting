from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service



# ChromeDriver パス設定
service = Service(executable_path="/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://rahulshettyacademy.com/client/")

driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("example@email.com")
driver.find_element(By.XPATH, "//form/div[2]/input").send_keys("123456")
driver.find_element(By.CSS_SELECTOR, "input[id='confirmPassword']").send_keys("123456")

driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()

input("Press Enter to exit...")


