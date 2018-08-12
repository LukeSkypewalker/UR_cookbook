# Echo client program
import socket
import time

HOST = "10.0.0.2"  # The remote host
PORT = 30002  # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

s.send(("speedj([0, 0, 0, 0, 0, 10], a=5.0, t=10)" + "\n").encode())

s.close()
