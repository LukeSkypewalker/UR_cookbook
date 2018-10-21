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

    vel = state.z
    print(vel)
    acc = 4
    t = 1

    cmd = "speedj([0, {j1}, {j2}, {j3}, 0, 0], {acc}, {time})\n".format(j1=-vel, j2=vel*2, j3=-vel, acc=acc, time=t)
    s.send((cmd).encode())
    data = s.recv(1024)

s.close()
