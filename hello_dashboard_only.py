# Dashboard examples
# https://www.universal-robots.com/how-tos-and-faqs/how-to/ur-how-tos/dashboard-server-port-29999-15690/
import socket

HOST = "10.0.0.2"
PORT = 29999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# s.send(("unlock protective stop\n").encode())
# s.send(("stop\n").encode())
s.send(("play\n").encode())
#s.send(("pause\n").encode())
