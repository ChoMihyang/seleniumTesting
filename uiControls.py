from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service



# ChromeDriver パス設定
service = Service(executable_path="/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Checkbox 
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break


# Radiobutton
radio_buttons = driver.find_elements(By.XPATH, "//input[@type='radio']")

for radio_button in radio_buttons:
    if radio_button.get_attribute("value") == "radio2":
        radio_button.click()
        assert radio_button.is_selected()
        break


assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert driver.find_element(By.ID, "displayed-text").is_displayed() # False