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

    vel = 0.1
    acc = 0.5
    rad_vel = 1
    t = 1

    x = 0
    y = 0
    z = 0
    rx = 0
    ry = 0
    rz = 0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x = -vel
    if keys[pygame.K_RIGHT]:
        x = vel
    if keys[pygame.K_UP]:
        y = vel
    if keys[pygame.K_DOWN]:
        y = -vel
    if keys[pygame.K_PAGEUP]:
        z = vel
    if keys[pygame.K_PAGEDOWN]:
        z = -vel
    if keys[pygame.K_q]:
        rx = -rad_vel
    if keys[pygame.K_w]:
        rx = rad_vel
    if keys[pygame.K_a]:
        ry = -rad_vel
    if keys[pygame.K_s]:
        ry = rad_vel
    if keys[pygame.K_z]:
        rz = -rad_vel
    if keys[pygame.K_x]:
        rz = rad_vel

    cmd = "speedl([{x},{y},{z}, {rx}, {ry}, {rz}], {acc}, {time})\n".format(x=x, y=y, z=z, rx=rx, ry=ry, rz=rz, acc=acc, time=t)
    s.send((cmd).encode())
    data = s.recv(1024)

    screen.fill((0, 0, 0))
    pygame.display.flip()
