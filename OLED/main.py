from machine import Pin, I2C
i2c = I2C(scl=Pin(5), sda=Pin(4))

from ssd1306 import SSD1306_I2C
oled = SSD1306_I2C(128, 64, i2c)

oled.fill(1)
oled.show()
oled.fill(0)
oled.show()

oled.pixel(0, 0, 1)
oled.show()
oled.pixel(127, 63, 1)
oled.show()

oled.text('Hello', 0, 0)
oled.text('World', 0, 10)
oled.show()

oled.invert(True)
oled.invert(False)

