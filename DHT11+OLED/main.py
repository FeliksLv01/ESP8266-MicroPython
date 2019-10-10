import time
from ssd1306 import SSD1306_I2C
import weather

oled.fill(0)
oled.show()


oled.text('Hello', 0, 0)
oled.text('World', 50, 0)
oled.text('kcqnly',80,50)
oled.show()
time.sleep(2)
oled.fill(1)
oled.show()
time.sleep(1)
oled.fill(0)
oled.show()
oled.text('waiting...',0,0)
oled.show()
time.sleep(2)


weather.showdata()
