from utilities.baseClass import BaseClass


# @pytest.mark.usefixtures("setup")
# fixtureを定義したClassを継承する
class TestOne(BaseClass):
    def test_e2e(self, setup):
        print("dd")



