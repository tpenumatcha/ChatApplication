from flask import Blueprint, request
from socket_server.client import Client
from .database import Database
import json
import time

clients = {}
views = Blueprint('views', __name__)
db = Database()


@views.route('/')
def home():
    return "<h1>Default</h1>"


@views.route('/add', methods=["POST", "GET"])
def new_user():
    print(clients)
    #print(request.json['user'])
    user = request.json['user']['username']
    group_id = request.json['user']['group_id']
    new_client = Client(user, group_id)
    clients[user] = new_client
    print(new_client.all_messages())
    time.sleep(20)
    entry = {'user': user, 'group': group_id, 'message': new_client.all_messages()[-1]}
    db.add_entry(entry)
    print(db.recieve_messages(group_id))
    return '200'


@views.route('/send', methods=['POST', 'GET'])
def send():
    message = request.json['message']['message']
    group = request.json['message']['group']
    user = request.json['message']['user']
    clients[user].send_message(message)
    time.sleep(20)
    entry = {'user': user, 'group': group, 'message': clients[user].all_messages()[-1]}
    db.add_entry(entry)
    return '200'



@views.route('/delete', methods=["POST", "GET"])
def delete_user():
    user = request.json['user']
    del clients[user]
    db.delete_user(user)


@views.route('/get_messages/<group>',  methods=['GET', 'POST'])
def get_messages(group):
    #print(clients[user])
    #print(clients[user].all_messages())
    messages = []
    result = db.recieve_messages(group)
    for each in result:
        messages.append(each['message'])
    return json.dumps({'messages': messages})


