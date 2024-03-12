from umqttsimple import MQTTClient
import machine
import ubinascii
try:
    import usocket as socket
except KeyboardInterrupt:
    import socket

import network
import esp

esp.osdebug(None)

import gc

gc.collect()

ssid = 'LAB DOANH NGHIEP'
password = 'E202DHKH'
mqtt_server = '10.10.84.116'

client_id = ubinascii.hexlify(machine.unique_id())
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect(ssid, password)

while not sta.isconnected():
    pass

print('Đã kết nối đến wifi:', ssid)
print(sta.ifconfig())
def web_page():
    html_flie = """
  <html>
  <head>
  <meta name="viewport" content="width=device-width, initial-scale=1", charset="utf-8">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://pyscript.net/releases/2024.1.1/core.css" />
    <script type="module" src="https://pyscript.net/releases/2024.1.1/core.js"></script>

  <style>
    body{
      background: linear-gradient(to left, grey, rgba(128, 128, 128, 0));
      font-family: Roboto;
      height: 900px;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-direction: column;
      row-gap: 5px;
    }
    .tittle{
      font-size: 18px;
      font-weight: bold;
      display: flex;
      justify-content: center;
    }
    .button-section{
      display: flex;
      flex-direction: column;
      row-gap: 20px;
      padding-left: 20px;
      padding-right: 20px;
    }
    .container{
      width: 300px;
      box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.5);
      border: 2px solid grey;
      display: flex;
      flex-direction: column;
      padding: 25px;
      border-radius: 5px;
      row-gap: 20px;
    }
    .led_main,.ledD0,.ledD1,.Traffic{
      display: flex;
      column-gap: 10px;
    }
    .led-button,.ledD0-button,.ledD1-button,.led-traffic-button{
      display: flex;
      flex: 1;
      column-gap: 10px;
      justify-content: end;
    }
    .stats{
      flex: 1;
      display: flex;
      justify-content: end;
    }
    .weather-forecast{
      display: flex;
      flex-direction: column;
      width: 300px;
      border: 2px solid grey;
      box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.4);
      padding: 25px;
      border-radius: 5px;
      row-gap: 15px;
    }
    .Tittle{
      font-size: 20px;
      font-weight: bold;
      display: flex;
      justify-content: center;
    }
    .Stats{
      display: flex;
      flex-direction: column;
      row-gap: 18px;
    }
    .nhiet_do,.do_am{
      font-size: 18px;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="tittle">
      Demo ESP8266
    </div>
    <div class="button-section">
      <div class="led_main">
        <div class="stats">Led_Main:</div>
        <div class="led-button">
          <a href=\"?led_main=on\"><button>ON</button></a>
          <a href=\"?led_main=off\"><button>OFF</button></a>
        </div>
      </div>
      <div class="ledD0">
        <div class="stats">Led_D0:</div>
        <div class="ledD0-button">
          <a href=\"?led_D0=on\"><button>ON</button></a>
          <a href=\"?led_D0=off\"><button>OFF</button></a>
        </div>
      </div>
      <div class="ledD1">
        <div class="stats">Led_D1:</div>
        <div class="ledD1-button">
          <a href=\"?led_D1=on\"><button>ON</button></a>
          <a href=\"?led_D1=off\"><button>OFF</button></a>
        </div>
      </div>

      <div class="Traffic">
        <div class="stats">Mod Nháy Đèn: </div>
        <div class="led-traffic-button">
          <a href=\"?Mod_crazy=on\"><button>Alabatrap</button></a>
          <a href=\"?Mod_crazy=off\"><button>OFF</button></a>
        </div>
      </div>
    </div>
  </div>
  <div class="weather-forecast">

    <div class="Tittle">
      Cảm Biến Dự Báo Thời Tiết
    </div>

    <div class="Stats">
      <div class="description">
        <div class="nhiet_do">Nhiệt độ hiện tại là: %nhietdo%°C</div>
        <div class="do_am">Độ ẩm hiện tại là:%doam% %</div>
      </div>
    </div>

  </div>
</body>
</html>"""
    return html_flie
#0108675083