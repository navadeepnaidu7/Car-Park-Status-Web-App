import network
import time

def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)

    if not wlan.isconnected():
        print('Connecting to WiFi...')
        wlan.active(True)
        wlan.connect(ssid, password)

        timeout = 20  # seconds
        start_time = time.time()

        while not wlan.isconnected() and (time.time() - start_time) < timeout:
            print('Waiting for connection...')
            time.sleep(1)

        if wlan.isconnected():
            print('Connected to WiFi')
            print('Network config:', wlan.ifconfig())
        else:
            print('Failed to connect to WiFi within the timeout period.')

# Replace 'your_wifi_ssid' and 'your_wifi_password' with your actual Wi-Fi credentials
wifi_ssid = 'ssid'
wifi_password = 'password'

connect_to_wifi(wifi_ssid, wifi_password)

