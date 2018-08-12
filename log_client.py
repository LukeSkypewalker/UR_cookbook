import threading
import socket
import queue
import urx
import math3d as m3d
from lxml import etree
from time import sleep
import datetime

# Networking
# ============================================
keep_alive_timeout = 10


def connection_routine():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(3)
            s.connect(('localhost', 50000))
            # s.connect(('10.0.0.2', 2850))
            print("Connected")
            s.settimeout(None)

            threading.Thread(target=send_keep_alive, args=(s,)).start()
            while True:
                sleep(10)

        except socket.error:
            print(datetime.datetime.now(), "Socket connection error. Trying to reconnect..")
            sleep(1)
            s.close()
            pass


# explicit keep-alive is a demand from a Giesecke machine
def send_keep_alive(s):
    while True:
        try:
            s.send("<KeepAlive>StillHere</KeepAlive>".encode())
            sleep(keep_alive_timeout)
        except socket.error:
            return


# ============================================
# End of Networking


if __name__ == "__main__":

    threading.Thread(target=connection_routine).start()

    while True:
        sleep(1)
