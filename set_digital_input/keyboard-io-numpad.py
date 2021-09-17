import os
import socket
import pygame


def set_digital_in(socket, port, value):
    cmd = "sec di():\nset_digital_in({port}, {val})\nend\n".format(port=port, val=value)
    socket.send(cmd.encode())
    data = socket.recv(1024)


def set_digital_inputs(states):
    for i, item in enumerate(states):
        set_digital_in(s, i, states[i])


def draw_dashboard():
    for i, item in enumerate(states):
        pygame.draw.circle(screen, (100, 100, 100), (int(size/2), int(i*size+size/2)), size/2, int(size*0.1))


def draw_states(states):
    for i, state in enumerate(states):
        color = (0, 0, 0)
        if state:
            color = (0, 200, 0)
        pygame.draw.circle(screen, color, (size/2, i*size+size/2), size*0.4)


states = [False, False, False, False, False, False, False, False]
keys = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8]

HOST = "127.0.0.1"  # The remote host
PORT = 30003  # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 0)
pygame.init()
size=20
screen = pygame.display.set_mode((size,size*len(states)))
draw_dashboard()
running = True


while running:

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False

        if i.type == pygame.KEYDOWN:
            for n, key in enumerate(keys):
                if i.key == key:
                    states[n] = not states[n]

    set_digital_inputs(states)
    draw_states(states)
    pygame.display.flip()
