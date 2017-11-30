import socket
import threading
from time import sleep

import sys

from rmonitor.settings.settings import *


class Server(object):

    @staticmethod
    def on_new_client(conn, num_clients):
        try:
            # Sending message to connected client
            conn.send(b'Welcome to the local test RMonitor server.\n')

            # Keep the connection open until it runs out of messages
            playback_enabled = True
            num_clients = str(num_clients)

            while playback_enabled:
                message = 'Playback file: %s\n' % PLAYBACK_MESSAGES
                conn.send(message.encode())

                # Read up the file
                with open(PLAYBACK_MESSAGES) as tm:
                    msg_count = 0

                    # Read every line
                    for message in tm.readlines():
                        # Send to the client
                        logger.info('Client-%s - Message-%s - `%s`' % (num_clients, str(msg_count), message.strip('\n')))
                        conn.send(message.encode())
                        msg_count += 1

                        # Allow for faster variable playback speed
                        sleep(1 / PLAYBACK_SPEED)

                    playback_enabled = False

            # Out of messages
            conn.send(b'Playback has ended.\n')

        except Exception as e:
            logger.error(e)

            # Broke out of loop or Exception
            conn.send(b'Goodbye.\n')
            conn.close()

        finally:
            logger.info('Finished playback, exiting.')

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
        except socket.error as e:
            logger.debug('Bind failed:', e)
            sys.exit()

        logger.debug('Socket bind complete.')

        # Start listening on socket
        s.listen(10)
        logger.debug('Socket now listening.')

        # TODO: Create list of threads for better management
        # and cleaner exit with joins
        num_clients = 0
        while True:
            # Block and wait to accept new client connections
            conn, address = s.accept()
            logger.debug('Connected with ' + address[0] + ':' + str(address[1]))

            # Spin off new thread to handle
            threading.Thread(target=Server.on_new_client, args=(conn, num_clients)).start()

            num_clients += 1
