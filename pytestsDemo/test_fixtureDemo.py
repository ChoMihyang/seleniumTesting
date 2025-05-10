import pytest

@pytest.mark.usefixtures("setup")
class TestExample:
    
    # self: Classを定義するなら、全てのメソッドのパラメータとして必須入力
    def test_fixtureDemo(self):
        print("I will excute steps in fixtureDemo method")

    def test_fixtureDemo1(self):
        print("I will excute steps in fixtureDemo1 method")

    def test_fixtureDemo2(self):
        print("I will excute steps in fixtureDemo2 method")

    def test_fixtureDemo3(self):
        print("I will excute steps in fixtureDemo3 method")