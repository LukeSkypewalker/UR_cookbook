import keyboard
import pyperclip
import re
import urx


def send_to_dashboard(cmd='stop'):
    rob.dashboard.send_command(cmd)


def pos_to_clipboard(is_joints=False, only_xyz=True):
    pos = rob.getj() if is_joints else rob.getl()
    if only_xyz: pos = pos[:3]
    pyperclip.copy(str(pos))


def move():
    str = pyperclip.paste()
    str.strip()
    str_list = str.split(",")
    pose = [float(i) for i in pyperclip.paste().split(',')]
    print(pose)
    rob.movel(pose, acc=0.2)


rob = urx.Robot("10.0.0.2", use_rt=True)
rob.set_tcp((0, 0, 0.067, 1.57, 0, 0))

keyboard.add_hotkey('ctrl+win+q', pos_to_clipboard, args=(False, False), trigger_on_release=False)
keyboard.add_hotkey('ctrl+win+e', pos_to_clipboard, args=(True, False), trigger_on_release=False)
keyboard.add_hotkey('ctrl+win+shift+q', move, trigger_on_release=False)
keyboard.wait('ctrl+shift+esc')
