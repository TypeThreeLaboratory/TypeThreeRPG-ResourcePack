import shutil
import os
import logging

FILE_NAME = 'TypeThreeRPG-Pack'

FORMAT = '%(asctime)s [%(levelname)s]:%(message)s'

logging.basicConfig(format=FORMAT, level=logging.DEBUG)

logging.info("zipファイルにしています...")
shutil.make_archive(FILE_NAME, format='zip', root_dir='pack')

logging.info("zipファイルが生成されました")

logging.info("ファイルの場所:\n" + os.path.abspath('TypeThreeRPG-Pack.zip'))
