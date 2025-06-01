from utilities.baseClass import BaseClass
from pageObject.homePage import Homepage
from testData.homePageData import HomePageData
import pytest



class TestHomePage(BaseClass):
    def test_formSubmission(self, getData):
        homepage = Homepage(self.driver)
        homepage.getName().send_keys(getData["name"])
        homepage.getEmail().send_keys(getData["email"])
        homepage.getCheckbox().click()
        self.selectOptionByText(homepage.getGender(), getData["gender"])
        homepage.getSubmit().click()

        alertText = homepage.getSuccessMessage().text
        
        assert ("Success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param