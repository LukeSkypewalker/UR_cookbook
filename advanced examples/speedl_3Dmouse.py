import socket
import spacenavigator


HOST = "10.0.0.2"  # The remote host
PORT = 30003  # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

is_success = spacenavigator.open()
if not is_success:
    exit()

while 1:
    state = spacenavigator.read()
    # time.sleep(0.1)

    x = state.x/5
    y = state.y/5
    z = state.z/5
    print(x, y, z)

    vel = 0.1
    acc = 2
    t = 1

    cmd = "speedl([{x},{y},{z}, 0, 0, 0], {acc}, {time})\n".format(x=x, y=y, z=z, acc=acc, time=t)
    s.send((cmd).encode())
    data = s.recv(1024)

s.close()
