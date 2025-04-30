from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service



# ChromeDriver パス設定
service = Service(executable_path="/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://rahulshettyacademy.com/angularpractice/")

#locators: ID, name, Class Name, Xpath, CSS Selector, linkText
driver.find_element(By.NAME, "email").send_keys("hello@email.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

# Xpath, CSS Selector: seleniumがサポートしない要素にアクセスするために使用。全ての属性に使用可能
# Xpath　　　　　: //tagname[@attribute='value']
# CSS Selector: tagname[attribute='value'], #id, .classname
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("hello")
# Radiobutton
driver.find_element(By.XPATH, "//input[@id='inlineRadio1']").click()

# Static Dropdown: Select objectを使用して、ドロップダウンリストを操作する
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
# select_by_index, select_by_visible_text, select_by_value を使用
# dropdown.select_by_index(1) # インデックスで選択
dropdown.select_by_visible_text("Male") # 画面に見えるテキストで選択

# submit
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("helloagain")
# driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()

input("Press Enter to exit...")