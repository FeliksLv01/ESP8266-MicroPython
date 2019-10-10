from machine import Pin
import time

led = Pin(5,Pin.OUT)

while 1:
  led.on()
  time.sleep_ms(200)
  led.off()
  time.sleep_ms(200)


