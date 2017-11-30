import logging

logging.basicConfig(format='%(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger()


#ADDRESS = "50.56.75.58:50095"
ADDRESS = "127.0.0.1:5000"
HOST, PORT = ADDRESS.split(":")

TIMEOUT = 5

# 1 = real time, 5 = ~5x, 10 = ~10x, etc.
PLAYBACK_SPEED = 10
PLAYBACK_MESSAGES = './data/playback/2009 Sebring Test ALMS Session 4 - 0800-1000.txt'
