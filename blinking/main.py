# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import bluetooth
import glue

#data = {
#    'protocol': {
#        'name': 'bluetooth',
#        # device address
#        'addr': '/dev/ttyACM0',
#    },
#}

data = {
    'protocol': {
        'name': 'bluetooth',
        # mac adress of bluetooth device
        'addr': '00:12:10:17:01:76',
        'port': 1
    },
    'system': {
        'name': 'arduino',
    }
}
system = glue.connect(data)


class Main(BoxLayout):
    def toggle_blink(self):
        global board
        if self.button.state == 'normal':
            # stop blinking
            self.button.background_color = [1, 1, 1, 1]
            self.button.text = 'OFF'
            self.blink(False)
        else:
            self.button.background_color = [1, 0, 0, 1]
            # start to blink
            self.button.text = 'ON'
            self.blink(True)

    def blink(self, activate):
        global board
        if activate:
            board.digital[12].write(1)
        else:
            board.digital[12].write(0)
            #global blink_active
            #blink_active = activate
            #arduino_update_blink()


class BlinkingApp(App):
    def build(self):
        main = Main()
        return main

if __name__ == '__main__':
    app = BlinkingApp()
    app.run()