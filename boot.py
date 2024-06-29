try:
  import usocket as socket
except:
  import socket
  
import network
from machine import Pin

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'DEF2'
password = 'nv6543210'
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect(ssid, password)

while sta.isconnected() == False:
  pass
print('Ket noi mang Wifi thanh cong!')
print(sta.ifconfig())
