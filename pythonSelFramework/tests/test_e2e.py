from utilities.baseClass import BaseClass
from pageObject.homePage import Homepage
from pageObject.checkoutPage import CheckoutPage


# @pytest.mark.usefixtures("setup")
# fixtureを定義したClassを継承する
class TestOne(BaseClass):
    def test_e2e(self):
        homePage = Homepage(self.driver)
        checkOutPage = homePage.shopItem()
        cards = checkOutPage.getCardTitles()

        i = -1
        for card in cards:
            i += 1
            cardText = card.text
            print(cardText)
            if cardText == "Blackberry":
                checkOutPage.getCardFooters()[i].click()
        
        
        # confirmPage = checkOutPage.checkOutItems()
        # self.verifyLinkPresence("keyword")
        print("done")



