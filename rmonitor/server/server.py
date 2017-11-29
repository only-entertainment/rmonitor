import socket
import threading
from time import sleep

import sys

from rmonitor.settings.settings import *


class Server(object):

    @staticmethod
    def _on_new_client(conn):
        try:
            # Sending message to connected client
            conn.send(b'Welcome to the local test RMonitor server.\n')

            # Keep the connection open until it runs out of messages
            playback_enabled = True
            while playback_enabled:
                conn.send(b'Playback file: %s.\n' % PLAYBACK_MESSAGES)

                with open(PLAYBACK_MESSAGES) as tm:
                    msg_count = 0

                    for message in tm.readlines():
                        logger.info('Sending message `%s` - `%s`' % (str(msg_count), message))
                        conn.send(message.encode())

                        msg_count += 1
                        sleep(1 / PLAYBACK_SPEED)
                    playback_enabled = False

            # Out of messages
            conn.send(b'Playback has ended.\n')

            # Cheat and close the connection
            #raise

        except Exception as e:
            print(e)

            # Broke out of loop or Exception
            conn.send(b'Goodbye.\n')
            conn.close()

    @staticmethod
    def serve():
        # Get and configure a socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        logger.debug('Socket created.')

        try:
            # Bind socket to local host and port
            s.bind((HOST, int(PORT)))
        except socket.error as msg:
            logger.debug('Bind failed:', msg)
            sys.exit()

        logger.debug('Socket bind complete.')

        # Start listening on socket
        s.listen(10)
        logger.debug('Socket now listening.')

        while True:
            # Accept new client connections, blocks
            conn, address = s.accept()
            logger.debug('Connected with ' + address[0] + ':' + str(address[1]))

            # Spin off new thread to handle
            threading.Thread(target=Server._on_new_client, args=(conn,)).start()
