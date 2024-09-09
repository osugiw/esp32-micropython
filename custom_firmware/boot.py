# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

import esp
import connection as wifi
import machine, os
from machine import Timer, Pin, ADC
import time
from module_sd_card import SD as SD
from temperature import dht11_sensor as dht
import sensor_max30102
import display_ssd1306

def timerCallback(t):
    print("This is timer test")

esp.osdebug(None)       # turn off vendor O/S debugging messages
esp.osdebug(0)          # redirect vendor O/S debugging messages to UART(0)
# machine.freq(240000000) # set the CPU frequency to 240 MHz
# wifi.connect()			# Wifi connection

# Timer(0).init(period = 2000, mode=Timer.PERIODIC, callback= timerCallback)	# Test timer
# while(1):
#     # Digital Input GPIO test
#     button = Pin(5, Pin.IN)
#     if (button.value() == 1):
#         print("Button pressed")

#     # ADC Reading data test
#     adc = ADC(Pin(5))
#     print("ADC in range 16 bit: {}".format(adc.read_u16()))
#     print("ADC in microvolts; {}".format(adc.read_uv()))  
#     time.sleep_ms(500)