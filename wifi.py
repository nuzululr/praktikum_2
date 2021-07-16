import machine
import time
from time import sleep
from machine import Pin
import network
led_obj = Pin(23, Pin.OUT)

SSID = "iPhone Asus"
PASSWORD = "ten101010"

wifi_obj = network.WLAN(network.STA_IF)
wifi_obj.active(True)
wifi_obj.connect(SSID, PASSWORD)
while wifi_obj.isconnected() == False:
    led_obj.value(1)  
while wifi_obj.isconnected() == True:
    led_obj.value(0)
    sleep(0.5)
    print("Connected...")
    print(wifi_obj.ifconfig())
