from machine import Pin
import onewire
import ds18x20
import time
 
ow = onewire.OneWire(Pin(2))
ds=ds18x20.DS18X20(ow)
roms=ds.scan()
while True:
  ds.convert_temp()
  for rom in roms:
    print(ds.read_temp(rom))
  time.sleep(1)
