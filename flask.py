from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# Initialize parking status variable
parking_status = ["N/A"] * 4  # Initialize with placeholders

@app.route('/')
def index():
    # Pre-process data to include index and pass it to the template
    processed_data = [{'slot': i + 1, 'status': status} for i, status in enumerate(parking_status)]
    return render_template('index.html', parking_status=processed_data)

@app.route('/status', methods=['POST'])
def receive_status():
    global parking_status
    data = request.get_json()
    print("Received Data:", data)

    # Ensure that the received data is a list of the correct length (4 in this case)
    if isinstance(data, list) and len(data) == 4:
        # Update parking status with the raw data
        parking_status = data

        # Emit the updated status to connected clients using Socket.IO
        socketio.emit('update_status', {'parking_status': parking_status}, namespace='/test')

        return jsonify({"message": "Data received successfully"})

    return jsonify({"error": "Invalid data format"}), 400

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
