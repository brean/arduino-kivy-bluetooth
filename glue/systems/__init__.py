# -*- coding: utf-8 -*-
"""
board and system implementations, classes and functions that provide information about your hardware
"""
systems = {}


class System(object):
    def __init__(self, name, protocol):
        """
        communication with system
        """
        self.name = name
        self.protocol = protocol

try:
    # make sure you use my firmata-version that does not need to import serial if you want to build for kivy
    from pyfirmata import Board, BOARDS, BOARD_SETUP_WAIT_TIME

    class Arduino(System, Board):
        """
        firmata extension to use Bluetooth Socket for arduino
        connection
        """
        def __init__(self, sock):
            super(System, self).__init__('arduino', sock)
            self.sp = sock
            self.pass_time(BOARD_SETUP_WAIT_TIME)
            self.name = sock.name
            self.setup_layout(BOARDS['arduino'])
            # Iterate over the first messages to get firmware data
            while self.bytes_available():
                self.iterate()

    systems['arduino'] = Arduino
except ImportError as err:
    print err