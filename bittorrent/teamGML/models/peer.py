__author__ = 'LucaFerrari MarcoBersani GiovanniLodi'

from custom_utils.formatting import format_ip_address, format_port_number
from configurations import PORT

class Peer(object):

    def __init__(self, ip, port):
        self.ip = format_ip_address(ip)
        self.port = format_port_number(port)

    def __str__(self):
        return "%s:%s" % (self.ip, self.port)


    @classmethod
    def get_local_peer(cls):
        return Peer("127.0.0.0", PORT)