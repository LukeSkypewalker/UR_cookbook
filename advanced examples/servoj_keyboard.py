import socket
import pygame

HOST = "10.0.0.2"  # The remote host
PORT = 30003  # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


running = True
screen = pygame.display.set_mode((800, 600));

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False

    vel = 0
    acc = 5
    t = 1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        vel = 1
    if keys[pygame.K_DOWN]:
        vel = -1

    cmd = "speedj([0, {j1}, {j2}, {j3}, 0, 0], {acc}, {time})\n".format(j1=-vel, j2=vel*2, j3=-vel, acc=acc, time=t)
    s.send((cmd).encode())
    data = s.recv(1024)

    screen.fill((0, 0, 0))
    pygame.display.flip()
