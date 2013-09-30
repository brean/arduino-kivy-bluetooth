# -*- coding: utf-8 -*-
"""
board connection - provide classes to connect to some robotic board like arduino or raspberry py
directly via bluetooth or over TCP/IP
"""
from glue.protocols import protocols
from glue.systems import systems


def connect(data):
    """
    connect to system using protocol

    :param data: data that describes system and protocol
    """
    protocol_data = data['protocol']
    protocol = protocols[protocol_data['name']](protocol_data)

    system_data = data['system']
    system = systems[system_data['name']](protocol, system_data)

    return system