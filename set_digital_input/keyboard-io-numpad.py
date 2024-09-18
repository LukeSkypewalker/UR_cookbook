import os
import socket
import pygame


def main_loop():
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                for n, key in enumerate(keys):
                    if event.key == key:
                        states[n] = not states[n]
                        set_digital_in(s, n, states[n])
                        draw_states(n)
                        pygame.display.flip()


def set_digital_in(socket, port, value):
    cmd = "sec di():\nset_digital_in({port}, {val})\nend\n".format(port=port, val=value)
    socket.send(cmd.encode())
    socket.recv(1024)


def draw_init_screen():
    for i, state in enumerate(states):
        draw_states(i)
    pygame.display.flip()


def draw_states(i):
        color = (0, 0, 0)
        if states[i]:
            color = (0, 200, 0)
        pygame.draw.circle(screen, color, (size, i * size * 2 + size), size * 0.9)

        font = pygame.font.SysFont('arial', int(size * 1.5))
        text = font.render(str(i), True, (255, 255, 255))
        screen.blit(text, (int(size * 0.6), i * size * 2 + int(size * 0.3)))


states = []
keys = [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4,
        pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]
for key in keys:
    states.append(False)

# network
HOST = "127.0.0.1"  # The remote host
PORT = 30003
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# display
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 0)
pygame.init()
size = 12
width = size * 2
height = size * 2 * len(states)
screen = pygame.display.set_mode((width, height))

draw_init_screen()

main_loop()


