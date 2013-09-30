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

    class BluetoothSocket(bluetooth.BluetoothSocket, Protocol):
        def __init__(self, config):
            self.config = config
            self.name = config['name']
            super(BluetoothSocket, self).__init__()
            print (config['addr'], config['port'])
            self.connect((config['addr'], config['port']))

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
            return self.recv(numbytes=4096)

        def inWaiting(self):
            # XXX replace this with some real waiting state detection
            return 0

    protocols['bluetooth'] = BluetoothSocket
except ImportError as err:
    bluetooth = None
    print 'can not import bluetooth', err


try:
    import serial

    class SerialSocket(Protocol):
        def __init__(self, config):
            self.ser = serial.Serial(config['addr'], config['baudrate'])
            super(SerialSocket, self).__init__(self.ser.name)

        def write(self, data):
            self.ser.write(data)

        def inWaiting(self):
            # XXX replace this with some real wating state detection
            return 0

    protocols['serial'] = SerialSocket
except ImportError as err:
    socket = None
    print 'can not import socket', err


#sock = BTFirmataSock(bluetooth.RFCOMM)
#sock.connect((bd_addr, port))
#print 'Connected to {}'.format(bd_addr)
#sock.settimeout(1.0)
#board = BTArduino(sock)
