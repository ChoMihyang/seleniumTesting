import pytest

# setup()に定義されたコードの実行を、Class単位で行う
@pytest.fixture(scope="class")
def setup():
   print("I will be executing first")
   yield
   print("I will execute last")

@pytest.fixture
def dataLoad():
   print("user profile data is being created")
   return ["one", "two", "three.com"]

# 複数のデータを送るには、tupleフォーマットでパラメータ化する
@pytest.fixture(params=[("chrome", "Hi"), ("firefox", "SS"), ("IE", "DD")])
def crossBrowser(request):
   return request.param