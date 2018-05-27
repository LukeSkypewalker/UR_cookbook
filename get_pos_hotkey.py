import keyboard
import pyperclip
import urx


def send_to_dashboard(cmd='stop'):
    rob.dashboard.send_command(cmd)


def pos_to_clipboard(is_joints=False, only_xyz=True):
    pos = rob.getj() if is_joints else rob.getl()
    if only_xyz: pos = pos[:3]
    pyperclip.copy(str(pos))


rob = urx.Robot("10.0.0.2", use_rt=True)
keyboard.add_hotkey('ctrl+win+q', pos_to_clipboard, args=(False, False), trigger_on_release=False)
keyboard.wait('ctrl+shift+esc')
