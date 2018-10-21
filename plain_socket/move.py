# Echo client program
import socket
import time

HOST = "10.0.0.2"  # The remote host
PORT = 30002  # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

move_cmd1 = "movej([1, -1, 2, -1, 1, 0], a=0.3, v=1)\n"
move_cmd2 = "movel([2, -1, 1, 0, 2, 1], a=0.3, v=1)\n"

s.send(move_cmd1.encode())
# time.sleep(5) # without sleep between first command will be overwritten
s.send(move_cmd2.encode())

move_sequence = """
def move_sequence():\n 
    movej(p[0.3, 0.3, 0.3, 0, 0, 0], a=0.3, v=1)\n
    movel(p[0.2, 0.3, 0.3, 0, 0, 0], a=0.3, v=1)\n
end\n
"""

a = 0.2
v = 0.1
cmd = "movel([{x},{y},{z}, 0, 0, 0], {acc}, {vel})\n".format(x=0.3, y=0.2, z=0.4, acc=a, vel=v)

cmd = "speedj([0, 0, 0, 0, 0, 5], a=1.0, t=10)" + "\n"
cmd = "speedl([0.1, 0, 0, 0, 0, 0], a=1.0, t=10)" + "\n"


s.send((cmd).encode())
data = s.recv(1024)
s.close()
