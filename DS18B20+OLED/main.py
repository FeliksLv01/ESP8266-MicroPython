import time
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import onewire
import ds18x20

i2c = I2C(scl=Pin(5), sda=Pin(4))
oled = SSD1306_I2C(128, 64, i2c)
ow = onewire.OneWire(Pin(14))
ds = ds18x20.DS18X20(ow)
roms = ds.scan()

oled.fill(0)
oled.show()

oled.pixel(0, 0, 1)
oled.show()
oled.pixel(127, 63, 1)
oled.show()

oled.text('Hello', 0, 0)
oled.text('World', 50, 0)
oled.text('kcqnly',80,50)
oled.show()
time.sleep(2)
oled.fill(1)
oled.show()
while True:
    ds.convert_temp()
    for rom in roms:
        t = ds.read_temp(rom)
    time.sleep_ms(50)    
    oled.fill(0)
    oled.text("Temperature:" ,0, 0)
    oled.text("%.2f" % t, 80, 20)
    oled.show()
