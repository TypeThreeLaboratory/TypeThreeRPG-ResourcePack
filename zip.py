import shutil
import os
import logging

from time import sleep

FILE_NAME = 'TypeThreeRPG-Pack'

FORMAT = '%(asctime)s [%(levelname)s]:%(message)s'

logging.basicConfig(format=FORMAT, level=logging.DEBUG)
logging.info("実行開始")

logging.info("zipファイルにしています...")
shutil.make_archive(FILE_NAME, format='zip', root_dir='pack')

logging.info("zipファイルが生成されました")
logging.info("ファイルの場所:\n" + os.path.abspath('TypeThreeRPG-Pack.zip'))
logging.info("10秒後にこの画面を閉じます")

sleep(10)

logging.info("プログラムを終了します")