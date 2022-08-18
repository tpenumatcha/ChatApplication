from backend import create_app
from flask_socketio import SocketIO
from backend.database import Database

app = create_app()
socketio = SocketIO(app)
db = Database()


@socketio.on('event')
def handle_message_send(message_data_json, methods=['POST', 'GET']):
    message_data = dict(message_data_json)
    print("socket:" + message_data)



if __name__ == "__main__":
    db.drop()
    socketio.run(app, debug=True)
    #app.run(debug=True)