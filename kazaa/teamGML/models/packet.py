__author__ = 'LucaFerrari MarcoBersani GiovanniLodi'

import time

class Packet(object):

    def __init__(self, id, sender_ip = None):
        self.id = id
        self.sender_ip = sender_ip
        self.timestamp = time.time()