import machine
import time
from machine import Pin
from machine import UART
import json
import urequests

# Define the GPIO pins connected to your IR modules
ir_pins = [0, 1, 2, 3]  # Replace with your actual pin numbers

# Set up GPIO pins
ir_sensors = [Pin(pin, Pin.IN) for pin in ir_pins]

# Initialize UART for communication
uart = UART(0, baudrate=115200, tx=Pin(0), rx=Pin(1))

def get_parking_status():
    # Represent 'V' for 1 and 'O' for 0
    states = ['Vacant' if sensor.value() else 'Occupied' for sensor in ir_sensors]
    return states

while True:
    current_states = get_parking_status()
    print("Sensor Readings:", current_states)  # Debugging line

    # Send the data to the Flask server using urequests
    try:
        response = urequests.post('http://{IP ADDRESS OF YOUR DESKTOP PC}/status', json=current_states)
        print("Server Response:", response.text)  # Debugging line
        response.close()
    except Exception as e:
        print("Error:", e)

    time.sleep(0.1)

