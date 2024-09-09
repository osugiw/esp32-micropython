from machine import Pin, I2C
import ssd1306

# using default address 0x3C
i2c = I2C(sda=Pin(8), scl=Pin(9))
display = ssd1306.SSD1306_I2C(128, 64, i2c)
display.text('Hello, World!', 0, 0, 1)
display.show()

# draw another FrameBuffer on top of the current one at the given coordinates
import framebuf
fbuf = framebuf.FrameBuffer(bytearray(8 * 8 * 1), 8, 8, framebuf.MONO_VLSB)
fbuf.fill(1)
display.blit(fbuf, 10, 10, 0)           # draw on top at x=10, y=10, key=0
display.show()