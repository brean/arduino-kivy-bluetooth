# -*- coding: utf-8 -*-
"""
provide classes for different connection protocols
(bluetooth, tcp/ip, ...)
"""
protocols = {}


class Protocol(object):
    def __init__(self, name):
        """
        basic protocol interface
        """
        self.name = name

    def write(self, data):
        """
        write data to connected system
        """
        return False

    def read(self):
        """
        read data from connected system
        """
        return None


try:
    import bluetooth

    class BluetoothSocket(Protocol, bluetooth.BluetoothSocket):
        def __init__(self):
            super(self, BluetoothSocket).__init__(self.getsockname())

        def write(self, data):
            """
            write data to system
            :param data: data to send to the system
            """
            self.send(data)

        def read(self):
            """
            read data from system
            :return: received data
            """
            return self.recv()

        def inWaiting(self):
            # XXX replace this with some real waiting state detection
            return 0

    protocols['bluetooth'] = BluetoothSocket
except ImportError as err:
    print 'can not import bluetooth', err


try:
    import socket

    class Socket(Protocol):
        def __init__(self):
            super(self, Socket).__init__(self.getsockname())

        def write(self, data):
            self.send(data)

    def inWaiting(self):
        # XXX replace this with some real wating state detection
        return 0

    protocols['socket'] = Socket
except ImportError as err:
    print 'can not import socket', err

#sock = BTFirmataSock(bluetooth.RFCOMM)
#sock.connect((bd_addr, port))
#print 'Connected to {}'.format(bd_addr)
#sock.settimeout(1.0)
#board = BTArduino(sock)