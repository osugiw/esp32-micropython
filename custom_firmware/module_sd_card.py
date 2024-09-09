# SD()

from machine import Pin, SDCard
import os

# SD Card test with modifying SPI pins by software
class SD:
    def __init__(self, _cs=15, _miso=13, _mosi=11, _sck=12):
        self.sd = SDCard(slot=2, cs=Pin(_cs), miso=Pin(_miso), mosi=Pin(_mosi), sck=Pin(_sck), freq=18000000)
        os.mount(self.sd, '/sd')
#         print(uos.listdir("/"))                                                                                    
    
    def readDir(self, dirPath):
        print(uos.listdir(dirPath))
    
    def mount(self):
        os.mount(self.sd, "/sd")