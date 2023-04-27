import time
import os
import sys
import socket
import random
import string
try:
    import requests
except ImportError:
    os.system("pip install requests")

class DoS_example:
    def __init__(self, ip:str=None, port:str=None, url:str=None, filesize:int=50) -> None:
        self.ip = ip
        self.port = port
        self.url = url
        self.sendranfile = random.sample(string.ascii_letters + string.digits, filesize)
        print(self.sendranfile)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def socket_attrack(self):
        port = 1
        while True:
            self.sock.connect(self.ip)


if __name__ == "__main__":
    DoS_example()