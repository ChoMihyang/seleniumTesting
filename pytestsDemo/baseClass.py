import logging
import inspect

class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        # ログを表示するファイルを指定
        fileHandler = logging.FileHandler('logfile.log') 

        # ログのフォーマットを指定
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)

        # filehandler objectを作成
        logger.addHandler(fileHandler)

        # ログのレベルを指定
        # logging.INFOに指定すると、INFO以上のレベル（2、3、4、5）のログが出力される
        logger.setLevel(logging.INFO)
        
        return logger