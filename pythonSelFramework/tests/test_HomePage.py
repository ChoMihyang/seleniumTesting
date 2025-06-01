from utilities.baseClass import BaseClass
from pageObject.homePage import Homepage
from selenium.webdriver.support.ui import Select



class TestHomePage(BaseClass):
    def test_formSubmission(self):
        homepage = Homepage(self.driver)
        homepage.getName().send_keys("My Name")
        homepage.getEmail().send_keys("myname@email.com")
        homepage.getCheckbox().click()
        self.selectOptionByText(homepage.getGender(), "Male")
        homepage.getSubmit().click()

        alertText = homepage.getSuccessMessage().text

