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
# configure pin 3 as servo
system.servo_config(3)

class Main(BoxLayout):
    def set_servo_pos(self, angle):
        system.digital[3].write(int(angle))


class ServoApp(App):
    def build(self):
        main = Main()
        return main

if __name__ == '__main__':
    app = ServoApp()
    app.run()
