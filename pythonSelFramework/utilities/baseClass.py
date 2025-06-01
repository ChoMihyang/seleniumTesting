import os
import pytest
import logging
import inspect
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


@pytest.mark.usefixtures("setup")
class BaseClass:
    # 明示的な待機を再使用できるよう一般化する
    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, text))
        )

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)



    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        if logger.handlers:
            logger.handlers.clear()

        # ログの出力先を指定
        file_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'utilities')
        os.makedirs(file_dir, exist_ok=True)
        
        # ログを表示するファイルを指定
        log_file = os.path.join(file_dir, 'logfile.log')
        fileHandler = logging.FileHandler(log_file)

        # ログのフォーマットを指定
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)

        # filehandler objectを作成
        logger.addHandler(fileHandler)

        # ログのレベルを指定
        # logging.INFOに指定すると、INFO以上のレベル（2、3、4、5）のログが出力される
        logger.setLevel(logging.INFO)
        
        return logger