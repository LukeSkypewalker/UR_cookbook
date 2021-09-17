# Echo client program
import socket
from time import sleep
import pynput
from pynput.mouse import Button
from pynput.keyboard import Key


mouse = pynput.mouse.Controller()
kb = pynput.keyboard.Controller()
dt = 0.5

HOST = "127.0.0.1"  # The remote host
PORT = 30002  # The same port as used by the server


def set_digital_in(socket, port, value):
    cmd = "sec di():\nset_digital_in(" + str(port) + ", " + value + ")\nend\n"
    socket.send(cmd.encode())
    data = socket.recv(1024)
    print("set_digital_in", port, value)
    #print("Received", repr(data))

def init_inputs():
    for i in range(15):
        set_digital_in(secondary, i, "False")

def init_scene():
    kb.press('`')
    kb.release('`')
    sleep(dt)
    kb.type('pv.set.palletizing_currentLayer_a 0')
    sleep(dt)
    kb.press(Key.enter)
    kb.release(Key.enter)
    sleep(dt)
    kb.type('pv.set.palletizing_currentUnit_a 0')
    sleep(dt)
    kb.press(Key.enter)
    kb.release(Key.enter)
    sleep(dt)
    kb.type('scene.restart')
    sleep(dt)
    kb.press(Key.enter)
    kb.release(Key.enter)
    sleep(dt)
    kb.press('`')
    kb.release('`')
    sleep(3)


def rocket():
    mouse.position = (1740, 70)
    mouse.click(Button.left, 1)
    sleep(3)

def play():
    mouse.position = (900, 70)
    mouse.click(Button.left, 1)
    sleep(2)

def play_sim():
    mouse.position = (870, 70)
    mouse.click(Button.left, 1)
    sleep(2)

def stop():
    mouse.position = (960, 70)
    mouse.click(Button.left, 1)


def test_reconnection():
    while True:
        rocket()
        # play()
        sleep(7)
        # stop()
        rocket()
        sleep(5)


def test_digital_input():
    while True:
        init_inputs()
        init_scene()
        rocket()
        sleep(1)
        play()
        sleep(5)
        set_digital_in(secondary, 0, "True")
        sleep(3)
        set_digital_in(secondary, 0, "False")
        sleep(10)
        set_digital_in(secondary, 0, "True")
        sleep(3)
        stop()
        sleep(1)
        rocket()


def blink():
    set_digital_in(secondary, 0, "True")
    sleep(3)
    set_digital_in(secondary, 0, "False")
    sleep(7)
    set_digital_in(secondary, 0, "True")
    sleep(1)
secondary = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

secondary.connect((HOST, PORT))
sleep(3)
# test_digital_input()


test_reconnection()

blink()

secondary.close()
