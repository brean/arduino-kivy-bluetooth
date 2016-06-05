# -*- coding: utf-8 -*-
"""
board and system implementations, classes and functions that provide
information about your hardware
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
    # make sure to use a firmata-version that does not need to import
    # serial if you want to build for kivy
    # ("import serial" will fail on normal kivy, see serial_test-project)
    # see https://github.com/brean/pyFirmata
    from pyfirmata import Board, BOARDS, BOARD_SETUP_WAIT_TIME

    class Arduino(Board, System):
        """
        firmata extension to use Bluetooth Socket for arduino
        connection
        """
        def __init__(self, protocol, config):
            self.config = config
            self.protocol = protocol
            super(Arduino, self).__init__(sp=protocol, layout=BOARDS['arduino'],
                                          name=protocol.name)
            self.sp = protocol
            self.pass_time(BOARD_SETUP_WAIT_TIME)
            self.setup_layout(BOARDS['arduino'])
            # Iterate over the first messages to get firmware data
            while self.bytes_available():
                self.iterate()
    systems['arduino'] = Arduino
except ImportError as err:
    print err
