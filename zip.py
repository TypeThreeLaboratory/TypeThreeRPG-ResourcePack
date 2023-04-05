import os
import logging
import zipfile
from time import sleep

#-----設定部分-----start

FORMAT = '%(asctime)s [%(levelname)s]:%(message)s'
FILE_NAME = 'TypeThreeRPG-Pack.zip'
ALLOW_LIST = ["pack.mcmeta", "pack.png", "LICENSE", "README.md"]

#-----設定部分-----end



logging.basicConfig(format=FORMAT, level=logging.DEBUG)
logging.info("実行開始")

def write(ziph, root, file):
    ziph.write(os.path.join(root, file))
    logging.info(root+"/" + file)


def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        dir = root.encode().decode()
        if (dir.startswith("assets", 2)):
            for file in files:
                write(ziph, root, file)
        elif (dir == "."):
            for file in files:
                for allowFile in ALLOW_LIST:
                    if (file == allowFile):
                        write(ziph, root, file)
                        continue


if __name__ == '__main__':
    logging.info("zipファイルにしています...")
    zipf = zipfile.ZipFile(FILE_NAME, 'w', zipfile.ZIP_DEFLATED)
    zipdir('.', zipf)
    zipf.close()

    logging.info("zipファイルが生成されました")
    logging.info("ファイルの場所:\n" + os.path.abspath(FILE_NAME))
    logging.info("10秒後にこの画面を閉じます")

    sleep(10)

logging.info("プログラムを終了します")
