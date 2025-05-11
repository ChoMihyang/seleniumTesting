import logging

def test_loggingDemo():
    logger = logging.getLogger(__name__)

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

    # ログレベル別の出力メッセージ指定
    logger.debug("This is a debug message")         # Level 1
    logger.info("This is an info message")          # Level 2
    logger.warning("This is a warning message")     # Level 3
    logger.error("This is an error message")        # Level 4
    logger.critical("This is a critical message")   # Level 5
