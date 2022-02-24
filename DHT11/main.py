from machine import Pin
import dht
import time

dht11 = dht.DHT11(Pin(5))

while True:
    try:
        dht11.measure()
        print("dht11 humidity:", dht11.humidity())
        print("dht11 temperature:", dht11.temperature())
        time.sleep(0.5)
    except:
        continue
