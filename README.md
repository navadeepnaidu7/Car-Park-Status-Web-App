# parking-status-project

# Car Park Status Web App

Real-time Parking Availability Web Application with IoT Integration.

## Overview

This web application provides real-time information about the parking status using IoT devices. It visualizes the parking slots and their availability dynamically.

## Features

- Real-time updates on parking slot status.
- Interactive interface for users to view and interact with parking status.
- Simulate car arrival to trigger status changes.

## Technologies Used

- Flask for the server-side application.
- MicroPython on Pico for IoT communication.
- Socket.IO for real-time communication.
- HTML, CSS, and JavaScript for the frontend.

## Setup Instructions

1. Clone the repository.
2. Set up the Flask server(flask.py) in vs code or your preferred environment.
3. Flash the MicroPython code(main.py) and internt.py to your Pico device.
4. First connect the Pico W to internet by running internet.py
5. Update the necessary configurations in the code like IP addresses, SSID and passwords.
6. Run the Flask server and open the web application(The IP will be visible on terminal of flask.py).

## Usage

- Open the web application in a browser.
- View real-time parking slot status.
- Simulate a car arrival to trigger changes.


## License

This project is licensed under the [MIT License](LICENSE).


## Contact

For issues or inquiries, please contact [Navadeep Naidu](https://github.com/navadeepnaidu7).

--
