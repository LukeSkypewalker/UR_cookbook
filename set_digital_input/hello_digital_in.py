# Echo client program
import socket

HOST = "127.0.0.1"  # The remote host
PORT = 30002  # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

cmd = """
sec di():\n 
    set_digital_in(1,True)\n
end\n
"""

s.send(cmd.encode())
data = s.recv(1024)
s.close()
print("Received", repr(data))
