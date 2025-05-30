from selenium.webdriver.common.by import By
from pageObject.confirmPage import ConfirmPage

class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkOutBtn = (By.XPATH, "//button[@class='btn btn-success']")
    
    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)
    
    def getCardFooters(self):
        return self.driver.find_elements(*CheckoutPage.cardFooter)
    
    def checkOutItems(self):
        self.driver.find_element(*CheckoutPage.checkOutBtn).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
