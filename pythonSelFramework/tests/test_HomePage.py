from utilities.baseClass import BaseClass
from pageObject.homePage import Homepage
import pytest



class TestHomePage(BaseClass):
    def test_formSubmission(self, getData):
        homepage = Homepage(self.driver)
        homepage.getName().send_keys(getData[0])
        homepage.getEmail().send_keys("myname@email.com")
        homepage.getCheckbox().click()
        self.selectOptionByText(homepage.getGender(), "Male")
        homepage.getSubmit().click()

        alertText = homepage.getSuccessMessage().text
        
        assert ("Success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=[("firstN", "middleN", "lastN"),("firstN2", "middleN2", "lastN2")])
    def getData(self, request):
        return request.param