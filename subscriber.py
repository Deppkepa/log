import time
import paho.mqtt.client as mqtt_client
import random
import logging
from logging.handlers import TimedRotatingFileHandler
import sys
import platform
import requests

broker="broker.emqx.io"

FORMATTER_STRING = "%(asctime)s — %(name)s — %(levelname)s — %(message)s"
FORMATTER = logging.Formatter(FORMATTER_STRING)
LOG_FILE = "my_app-test.log"

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
logger = get_logger("subscriber")
def get_id():
    url="http://127.0.0.1:8000/id"
    try:
        car = platform.platform()
        box=requests.get(url)
        if (box.status_code == 200):
            logger.info("id:" + " - " + box.text + " - " + car)
            return box.text
        else:
            logger.error(car + "Error server" + box.text)
    except Exception as e:
        car = platform.platform()
        logger.error(car + " - Server error: " + e)

id = get_id()
print(id)
def on_message(client, userdata, message):
    time.sleep(1)
    data = str(message.payload.decode("utf-8"))
    logger.info("received message = " + data + " - " + car + " - " + id)


client = mqtt_client.Client( mqtt_client.CallbackAPIVersion.VERSION1, id)
client.on_message=on_message
car = platform.platform()
logger.info("Connecting to broker" + broker + " - " + car)
client.connect(broker)
client.loop_start()

client.subscribe("lab/leds/state")
time.sleep(1800)
client.disconnect()
client.loop_stop()