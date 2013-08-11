from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time
from pyfirmata import util, Board, BOARDS, BOARD_SETUP_WAIT_TIME
import bluetooth  # python-bluez
import sys
from threading import Timer


class BTFirmataSock(bluetooth.BluetoothSocket):
    def write(self, data):
        sock.send(data)
        
    def inWaiting(self):
        # XXX replace this with some real wating state
        return 0


class BTArduino(Board):
    """
    firmata extension to use Bluetooth Socket for arduino
    connection
    """
    def __init__(self, sock):
        self.sp = sock
        self.pass_time(BOARD_SETUP_WAIT_TIME)
        self.name = sock.getsockname()
        self.setup_layout(BOARDS['arduino'])
        # Iterate over the first messages to get firmware data
        while self.bytes_available():
            self.iterate()


# mac adress of bluetooth device
bd_addr = '00:12:10:17:01:76'

port = 1
sock = BTFirmataSock( bluetooth.RFCOMM )
sock.connect((bd_addr, port))
print 'Connected to {}'.format(bd_addr)
sock.settimeout(1.0)
board = BTArduino(sock)

blink_state = False
blink_active = False

def arduino_blink():
    global blink_state
    global blink_active
    if blink_active:
        if blink_state:
            board.digital[12].write(1)
            board.digital[13].write(0)
        else:
            board.digital[12].write(0)
            board.digital[13].write(1)
        blink_state = not blink_state
        arduino_update_blink()
    else:
        board.digital[13].write(0)
        board.digital[12].write(0)

def arduino_update_blink():
    print 'blinking...'
    t = Timer(0.2, arduino_blink)
    t.start()


def arduino_reset_blink():
    global blink_active
    print 'stop blinking'
    blink_active = True


class Main(BoxLayout):
    def toggle_blink(self):
        if self.button.state == 'normal':
            # stop blinking
            self.button.background_color = [1,1,1,1]
            self.button.text = 'OFF'
            self.blink(False)
        else:
            self.button.background_color = [1,0,0,1]
            # start to blink
            self.button.text = 'ON'
            self.blink(True)
        
    def blink(self, activate):
        global blink_active
        blink_active = activate
        arduino_update_blink()
            

class RobotControlApp(App):
    def build(self):
        main = Main()
        return main

if __name__ == '__main__':
    app = RobotControlApp()
    app.run()
