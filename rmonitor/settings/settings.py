import logging

logging.basicConfig(format='%(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger()


ADDRESS = "50.56.75.58:50095"
HOST, PORT = ADDRESS.split(":")

SLEEP = 1.0
TIMEOUT = 5
