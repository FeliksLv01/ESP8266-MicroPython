from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from dht import DHT11
i2c = I2C(scl=Pin(14), sda=Pin(2))
oled = SSD1306_I2C(128, 64, i2c)
sensor = DHT11(Pin(5))
while True:
    try:
        sensor.measure()
        t = sensor.temperature()
        h = sensor.humidity()
        oled.fill(0)
        oled.text("T:{}".format(t), 0, 0)
        oled.text("H:{}".format(h), 0, 20)
        oled.show()
    except:
        continue
