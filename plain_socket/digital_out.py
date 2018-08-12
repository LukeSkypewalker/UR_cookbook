# Echo client program
import socket

HOST = "10.0.0.2"  # The remote host
PORT = 30002  # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

s.send(("set_digital_out(0,True)\n").encode())

data = s.recv(1024)
s.close()
print("Received", repr(data))
