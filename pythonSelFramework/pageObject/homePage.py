from selenium.webdriver.common.by import By
from pageObject.checkoutPage import CheckoutPage


# ホームページの要素（入力欄、ボタンなど）を定義するクラス
class Homepage:

    def __init__(self, driver):
        self.driver = driver

    # tuple形式で定義（Byの種類とセレクタを一緒に管理できるため）
    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    checkbox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.CSS_SELECTOR, "input[type='submit']")
    successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")

    def shopItem(self):
        self.driver.find_element(*Homepage.shop).click()
        checkOutPage = CheckoutPage(self.driver)
        return checkOutPage
    
    def getName(self):
        return self.driver.find_element(*Homepage.name)
    
    def getEmail(self):
        return self.driver.find_element(*Homepage.email)
    
    def getCheckbox(self):
        return self.driver.find_element(*Homepage.checkbox)
    
    def getGender(self):
        return self.driver.find_element(*Homepage.gender)
    
    def getSubmit(self):
        return self.driver.find_element(*Homepage.submit)
    
    def getSuccessMessage(self):
        return self.driver.find_element(*Homepage.successMessage)