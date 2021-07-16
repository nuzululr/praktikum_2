import machine
import time
from machine import Pin
from time import sleep

led_obj = Pin(22, Pin.OUT)

while True:
    led_obj.value(1)
    sleep(.25)
    led_obj.value(0)
    sleep(.25)
    led_obj.value(1)
    sleep(.25)
    led_obj.value(0)
    sleep(.25)
    led_obj.value(1)
    sleep(.25)
    led_obj.value(0)
    sleep(.25)
    led_obj.value(1)
    sleep(1)
    led_obj.value(0)
    sleep(1)
    led_obj.value(1)
    sleep(1)
    led_obj.value(0)
    sleep(1)
    led_obj.value(1)
    sleep(1)
    led_obj.value(0)
    sleep(1)
    
    
    