import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="class")
def setup(request):
    service = Service(executable_path="/usr/local/bin/chromedriver")
    driver = webdriver.Chrome(service=service)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    # class objectの'driver'に、fixture内objectの'driver'を代入する
    # これにより、今のfixtureを使うすべてのclass内の'driver'に、driver objectが代入される
    # setupメソッドのrequest変数を通して、'cls'変数にアクセスできる
    request.cls.driver = driver
    yield
    driver.close()
    