from selenium.webdriver.common.by import By
from pageObject.checkoutPage import CheckoutPage


# ホームページの要素（入力欄、ボタンなど）を定義するクラス
class Homepage:

    def __init__(self, driver):
        self.driver = driver

    # tuple
    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def shopItem(self):
        self.driver.find_element(*Homepage.shop).click()
        checkOutPage = CheckoutPage(self.driver)
        return checkOutPage