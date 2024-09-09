"""
# DHT Reading Test
_dht = dht(5)
while(1):
    _dht.read()
    time.sleep_ms(500)
"""

import dht
from machine import Pin
import time

class dht11_sensor:
    def __init__(self, _dhtPin):
        self.d = dht.DHT11(Pin(_dhtPin))

    def read(self):
        self.d.measure()
        time.sleep_ms(500)
        results = {"Temperature"	: self.d.temperature(),
                    "Humidity"		: self.d.humidity()}
        print("DHT11 reading - T:{}°, H:{}%".format(results["Temperature"], results["Humidity"]))
        return results
