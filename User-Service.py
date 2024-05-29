import logging
import sys
import hashlib
import datetime
import time
import platform
import uvicorn
from fastapi import FastAPI
from logging.handlers import TimedRotatingFileHandler
app = FastAPI()
FORMATTER_STRING = "%(asctime)s — %(name)s — %(levelname)s — %(message)s"
FORMATTER = logging.Formatter(FORMATTER_STRING)
LOG_FILE = "my_app-test.log"  # use fancy libs to make proper temp file
id_user = []

def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    logger.addHandler(console_handler)

    file_handler = TimedRotatingFileHandler(LOG_FILE, when='midnight')
    file_handler.setFormatter(FORMATTER)
    logger.addHandler(file_handler)

    return logger
logger = get_logger("User-Service")
@app.get('/id')
def id():
    time_str = str(datetime.datetime.now())
    box = hashlib.md5(time_str.encode()).hexdigest()
    car = platform.platform()
    logger.info("id generated" + " - " + car + " - " + box)
    for i in range(len(id_user)):
        if (id_user[i] != box):
            id_user.append(box)
            logger.info("id save" + " - " + car + " - " + box)
        else:
            logger.warning("id error. Re-creation id" + " - " + car + " - " + box)
            time_str = str(datetime.datetime.now())
            box = hashlib.md5(time_str.encode()).hexdigest()

    return box


if __name__ == "__main__":

    # logger = get_logger("my_app_logger")
    car = platform.platform()
    logger.info("Start logging" + " - " + car)
    logger.debug("Some debug message" + " - " + car)
    uvicorn.run(app, host="0.0.0.0", port=8000)
    # while True:
    #     try:
    #         time.sleep(1)
    #         logger.info("Keep logging")
    #     except KeyboardInterrupt:
    #         logger.fatal("User get bored")
    #         break