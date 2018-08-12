# Echo client program
import socket

HOST = "10.0.0."  # The remote host
PORT = 30002  # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
# s.send(("freedrive_mode()" + "\n" + "sleep(10)" + "\n").encode())


s.send(("def fd():\n" + "freedrive_mode()\n " + "sleep(1200)\n" + "end\n").encode())
s.send(("fd()").encode())
data = s.recv(1024)
s.close()
print("Received", repr(data))
