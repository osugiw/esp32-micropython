# MAX30102 = sensor_max30102.MAX30102_Sensor(8, 9, 400000)
# MAX30102.config_setup()
# MAX30102.read_data()

from max30102 import MAX30102
from machine import Timer, Pin, ADC, SoftI2C
from utime import ticks_diff, ticks_ms, ticks_us

# LED Power options
MAX30105_PULSE_AMP_LOWEST =  0x02 # 0.4mA  - Presence detection of ~4 inch
MAX30105_PULSE_AMP_LOW =     0x1F # 6.4mA  - Presence detection of ~8 inch
MAX30105_PULSE_AMP_MEDIUM =  0x7F # 25.4mA - Presence detection of ~8 inch
MAX30105_PULSE_AMP_HIGH =    0xFF # 50.0mA - Presence detection of ~12 inch

class MAX30102_Sensor:
    def __init__(self, _sda, _scl, _freq):
        self.sda = _sda
        self.scl = _scl
        self.freq = _freq
        
        # Samples initialization
        self.t_start = ticks_us()  # Starting time of the acquisition
        self.samples_n = 0  # Number of samples that have been collected
        
        # Initialize communication
        i2c = SoftI2C(sda=Pin(self.sda),
                      scl=Pin(self.scl),
                      freq=self.freq)
        self.sensor = MAX30102(i2c=i2c)
        self.sensor.setup_sensor()
        
    def config_setup(self, SAMPLE_AVG=8, ADC_RANGE=4096, SAMPLE_RATE=400, PULSE_WIDTH=118, LED_MODE=2,
                    LED_POWER=MAX30105_PULSE_AMP_LOW):
        # Set the number of samples to be averaged by the chip - Options: 1, 2, 4, 8, 16, 32
        self.sensor.set_fifo_average(SAMPLE_AVG)

        # Set the ADC range - Options: 2048, 4096, 8192, 16384
        self. sensor.set_adc_range(ADC_RANGE)

        # Set the sample rate - Options: 50, 100, 200, 400, 800, 1000, 1600, 3200
        self.sensor.set_sample_rate(SAMPLE_RATE)

        # Set the Pulse Width - Options: 69, 118, 215, 411
        self.sensor.set_pulse_width(PULSE_WIDTH)

        # Set the LED mode - Options: 1 (red), 2 (red + IR), 3 (red + IR + g - MAX30105 only)
        self.sensor.set_led_mode(LED_MODE)

        # Set the LED brightness of each LED
        self.sensor.set_pulse_amplitude_red(LED_POWER)
        self.sensor.set_pulse_amplitude_it(LED_POWER)
        self.sensor.set_pulse_amplitude_green(LED_POWER)

        # Set the LED brightness of all the active LEDs
        self.sensor.set_active_leds_amplitude(LED_POWER)
        
    def read_data(self):
        while (True):
            # The check() method has to be continuously polled, to check if
            # there are new readings into the sensor's FIFO queue. When new
            # readings are available, this function will put them into the storage.
            self.sensor.check()

            # Check if the storage contains available samples
            if (self.sensor.available()):
                # Access the storage FIFO and gather the readings (integers)
                red_sample = self.sensor.pop_red_from_storage()
                ir_sample = self.sensor.pop_ir_from_storage()

                # Print the acquired data (can be plot with Arduino Serial Plotter)
                print(red_sample, ",", ir_sample)

    def read_frequency(self):
        while (True):
            self.sensor.check()
            if (self.sensor.available()):
                # Compute the real frequency at which we receive data (with 999999 microsecond precision)
                if ticks_diff(ticks_us(), self.t_start) >= 999999:
                    f_HZ = self.samples_n
                    self.samples_n = 0
                    print("acqusition frequency = ", f_HZ)
                    self.t_start = ticks_us()
                    temperature_C = self.sensor.read_temperature()
                    print("Internal temperature = {}°".format(temperature_C))
                else:
                    self.samples_n = self.samples_n + 1
