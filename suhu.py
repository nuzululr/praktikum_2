import machine
import time
from machine import Pin
from time import sleep
import dht

dht22_obj = dht.DHT22(Pin(4))
led_obj = Pin(23, Pin.OUT)

while True:
    dht22_obj.measure()
    temp = dht22_obj.temperature()
    print(temp)
    sleep(0.5)
if temp > 35
    led_obj.value(1)
    sleep(.25)
if temp <= 35
    led_obj.value(0)
    sleep(.25)
    
    
    