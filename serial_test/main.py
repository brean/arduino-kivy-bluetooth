# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.label  import Label

import sys
msg = 'import ok'
try:
    # this will crash the android kivy launcher!
    import serial
except:
    msg = sys.exc_info()[1].msg


class SerialTestApp(App):
    def build(self):
        return Label(text=msg)

if __name__ == '__main__':
    SerialTestApp().run()
