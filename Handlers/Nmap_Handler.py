import os
import sys
from AppUtils import *

class Nmap():
    def __init__(self):
        self.Curr_Host = return_Curr_host()
        self.Alive_Hosts = [Host for Host in Host_IP_Generator(self.Curr_Host, 27) if Echo_Ping(Host)]
        print(self.Alive_Hosts)

Test = Nmap()       