# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import glue

# data = {
#     'protocol': {
#         'name': 'serial',
#         # device address
#         'addr': '/dev/ttyACM1',
#         'baudrate': 57600
#     },
#     'system': {
#         'name': 'arduino',
#     }
# }

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
        if self.button.state == 'normal':
            # stop blinking
            self.button.background_color = [1, 1, 1, 1]
            self.button.text = 'OFF'
            system.digital[12].write(0)
        else:
            self.button.background_color = [1, 0, 0, 1]
            # start to blink
            self.button.text = 'ON'
            system.digital[12].write(1)


class BlinkingApp(App):
    def build(self):
        main = Main()
        return main

if __name__ == '__main__':
    app = BlinkingApp()
    app.run()
