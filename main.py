from machine import Pin, Timer, PWM
from time import sleep
import dht

# Khai Báo Đèn
led = Pin(2, Pin.OUT, value=0)
led2 = Pin(5, Pin.OUT, value=1)
led3 = Pin(15, Pin.OUT, value=1)

# Đọc cảm ứng DHT11
sensor = dht.DHT11(Pin(16))
def read_dht11():
    sensor.measure()
    temperature = sensor.temperature()
    humidity = sensor.humidity()
    return temperature, humidity

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
   <script>
        function fetchData() {
            fetch('/data')
                .then(response => response.json())
                .then(data => {
                    document.getElementById('temperature').innerText = "Nhiệt độ hiện tại là: " + data.temperature + "°C";
                    document.getElementById('humidity').innerText = "Độ ẩm hiện tại là: " +  data.humidity + "%";
                })
                .catch(err => {
                    console.error('Error fetching data:', err);
                    document.getElementById('data').innerText = 'Error fetching data';
                });
        }
        setInterval(fetchData, 10000); // Lặp lại việc đo sensor sau mỗi 10s
        window.onload = fetchData;
    </script>
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

    <div id="data" class="Stats">
      <div class="description">
        <div id="temperature" class="nhiet_do">Loading Temperature.....</div>
        <div id="humidity" class="do_am">Loading Humidity......</div>
      </div>
    </div>

  </div>
  
  
</body>
</html>"""
    return html_flie


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
while True:

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


        if "/data" in request:
            temperature, humidity = read_dht11()
            response = {'temperature' : temperature, 'humidity' : humidity} #tạo thêm 1 dic để đưa lên JSON nhằm thay đổi theo dic
            conn.send('HTTP/1.1 200 OK\n')
            conn.send('Content-Type: text/html\n')
            conn.send('Connection: close\n\n')
            conn.sendall(str(response).replace("'", '"')) # Dùng để thay đổi file JSON nhằm update thông tin

        else:
            response = web_page()
            conn.send('HTTP/1.1 200 OK\n')
            conn.send('Content-Type: text/html\n')
            conn.send('Connection: close\n\n')
            conn.sendall(response)
        conn.close()

    except OSError as e:
        conn.close()
        print('Connection closed')