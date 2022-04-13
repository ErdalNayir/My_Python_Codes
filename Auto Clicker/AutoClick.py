# importing time and threading
import time
import threading
from pynput.mouse import Button, Controller
import keyboard

# pynput.keyboard is used to watch events of
# keyboard for start and stop of auto-clicker

# four variables are created to
# control the auto-clicker
delay = 0.5
button = Button.left
#start_stop_key = keyboard.add_hotkey('ctrl + c',)
#stop_key = keyboard.add_hotkey('ctrl + q')

# threading.Thread is used
# to control clicks
class ClickMouse(threading.Thread):
  # delay and button is passed in class
  # to check execution of auto-clicker
    def __init__(self, delay, button):
        super().__init__()

        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True
        self.count=0

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def start_stop_clicking(self):

        if self.count%2==0:
            self.start_clicking()
            self.count+=1
        else:
            self.stop_clicking()
            self.count+=1
    # method to check and run loop until
    # it is true another loop will check
    # if it is set to true or not,
    # for mouse click it set to button
    # and delay.
    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)

# instance of mouse controller is created
mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


keyboard.add_hotkey('ctrl + s',click_thread.start_stop_clicking)
#keyboard.add_hotkey('ctrl + h',click_thread.start_clicking)
keyboard.add_hotkey('ctrl + q',click_thread.exit)
