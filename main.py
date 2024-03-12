import asyncio
import random
import time
from umqttsimple import MQTTClient
from boot import *
from machine import Pin, Timer, PWM
from time import sleep
import dht

# Khai Báo Đèn
led = Pin(2, Pin.OUT, value=0)
led2 = Pin(5, Pin.OUT, value=1)
led3 = Pin(15, Pin.OUT, value=1)

# Nút ở chân sạc
button_main = Pin(0, Pin.IN)


def handle_interrupt():
    led.value(not led.value())


button_main.irq(trigger=3, handler=handle_interrupt)

# Đọc cảm ứng DHT11
sensor = dht.DHT11(Pin(16))
sensor.measure()
nhietdo = ''
doam = ''


def call_back(timer):
    tem = sensor.temperature()
    tem2 = sensor.humidity()
    return str(tem), str(tem2)


def handle(res1, res2):
    global nhietdo, doam
    nhietdo = res1
    doam = res2

#I'm Xuan Truong Commit
time = Timer(0)
time.init(period=1000, callback=lambda t: handle(*(call_back(t))))
sleep(1)

# --------------------------------------------------------------
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
while True:
    print("Nhiệt độ là:", str(nhietdo))
    print("Độ Ẩm là:", str(doam))
    try:
        if gc.mem_free() < 102000:
            gc.collect()
        conn, addr = s.accept()
        conn.settimeout(3.0)
        print('Got a connection from %s' % str(addr))
        request = conn.recv(1024)
        conn.settimeout(None)
        request = str(request)
        print('Content = %s' % request)

        led_main_on = request.find('/?led_main=on')
        led_D0_on = request.find('/?led_D0=on')
        led_D1_on = request.find('/?led_D1=on')

        led_main_off = request.find('/?led_main=off')
        led_D0_off = request.find('/?led_D0=off')
        led_D1_off = request.find('/?led_D1=off')

        Mod_on = request.find('/?Mod_crazy=on')
        Mod_off = request.find('/?Mod_crazy=off')

        if led_main_on == 6:
            print("Led_Main ON")
            led.value(0)
        if led_main_off == 6:
            print("Led_Main OFF")
            led.value(1)

        if led_D0_on == 6:
            led2.value(1)
        if led_D0_off == 6:
            led2.value(0)

        if led_D1_on == 6:
            led3.value(1)
        if led_D1_off == 6:
            led3.value(0)

        if Mod_on == 6:
            k = 0
            while k < 18:
                led2.value(not led2.value())
                sleep(0.1)
                led3.value(not led3.value())
                sleep(0.1)
                led.value(not led.value())
                k += 1

        if Mod_off == 6:
            led.value(1)
            led2.value(0)
            led3.value(0)

        response = web_page()
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()

    except OSError as e:
        conn.close()
        print('Connection closed')
