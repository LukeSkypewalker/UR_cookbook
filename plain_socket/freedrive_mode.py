# Echo client program
import socket

HOST = "10.0.0.2"  # The remote host
PORT = 30002  # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

freedrive = """
def freedrive():\n 
    freedrive_mode()\n
    sleep(60)\n
end\n
"""

# or you can concat strings:
prog = 'def freedrive():\n'
prog += 'freedrive_mode()\n'
prog += 'sleep(60)\n'
prog += "end\n"


s.send(freedrive.encode())
data = s.recv(1024)
s.close()
print("Received", repr(data))
