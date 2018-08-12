# Echo client program
import socket
import time

HOST = "10.0.0.2"  # The remote host
PORT = 30002  # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

s.send(("movej([1, -1, 2, -1, 1, 0], a=1.0, v=1)" + "\n").encode())
time.sleep(5)
s.send(("movej([2, -1, 1, 0, 2, 1], a=1.0, v=1)" + "\n").encode())
time.sleep(3)

s.close()
