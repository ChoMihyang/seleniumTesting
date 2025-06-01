import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = None

# pytestのコマンドラインオプションを追加する
def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    global driver
    service = Service(executable_path="/usr/local/bin/chromedriver")
    driver = webdriver.Chrome(service=service)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    # class objectの'driver'に、fixture内objectの'driver'を代入する
    # これにより、今のfixtureを使うすべてのclass内の'driver'に、driver objectが代入される
    # setupメソッドのrequest変数を通して、'cls'変数にアクセスできる
    request.cls.driver = driver
    yield
    driver.close()
    
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
   
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)
