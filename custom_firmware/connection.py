import network
import machine
import time

# Wifi Configuration
wifi = {"ssid" 		: "oswNetw",
        "password"	: "gangTengah"
}
# LED Pin
built_in_led = 4

def connect():
    wlan = network.WLAN(network.STA_IF)
    if not wlan.active() or not wlan.isconnected():
        wlan.active(True)
        print('connecting to:', wifi["ssid"])
        wlan.connect(wifi["ssid"], wifi["password"])
        while not wlan.isconnected():
            pass
    # Connected to WiFi
    machine.Pin(built_in_led, machine.Pin.OUT, value = 1)
    print("Connected to {} network config: {} ".format(wifi["ssid"], wlan.ifconfig()))
