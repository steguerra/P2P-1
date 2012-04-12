__author__ = 'luca'

import socket


def connect_socket(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # useful to avoid boring address already in use
    sock.connect((ip, int(port)))
    return sock