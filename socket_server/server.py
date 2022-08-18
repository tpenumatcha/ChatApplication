import threading
import socket
from user import User
from group import Group
import time


#global constants
DEFAULT_PORT = 5050
DEFUALT_SERVER = socket.gethostbyname(socket.gethostname()) #localhost
DEFUALT_ADDR = (DEFUALT_SERVER, DEFAULT_PORT)
FORMAT = "utf8"
DISCONNECT_MESSAGE = "#DISCONNECT"
MAX_CONNECTIONS = 50 #total number of connections to the local server
BUFSIZE = 512


group_error = Group('#ERROR', 20)

users = set()
groups = {"#ERROR": group_error}
users_lock = threading.Lock()


local_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

local_server.bind(DEFUALT_ADDR)

def start_server(server):
    server.listen(MAX_CONNECTIONS)

    while True:
        try:
            print("Listening")
            conn, addr = server.accept()
            with users_lock:
                user = User(conn, addr)
                users.add(user)
            thread = threading.Thread(target=handle_client, args=(user, ))
            thread.start()
        except:
            print("Server Crashed")
            #send this message to users
            break
        



def handle_client(user):
    print("handling")
    
    client = user.conn
    name = client.recv(BUFSIZE).decode(FORMAT)
    print("name recieved")
    user.set_name(name)
    group = client.recv(BUFSIZE).decode(FORMAT)
    
    print("group recieved")
    user.set_group_id(group)
    
    if group not in groups:
        new_group = Group(group, 10)
        new_group.add_user(user)
        groups[group] = new_group
        broadcast(bytes(f"{name} has joined {group}", FORMAT), user)
    elif not groups[group].at_limit():
        groups[group].add_user(user)
        broadcast(bytes(f"{name} has joined {group}", FORMAT), user)
    else:
        groups["#ERROR"].add_user(user)
        broadcast(bytes(f"Unable to join, {group} is currently at capacity", FORMAT), user)
        time.sleep(15)
        groups["#ERROR"].remove_user(user)
        client.close()


    
    print("welcome message sent")

    while True:
        message = client.recv(BUFSIZE).decode(FORMAT)

        if message == bytes(DISCONNECT_MESSAGE, FORMAT):
            broadcast(bytes(f"{name} has left {group}", FORMAT), user)
            time.sleep(10)
            users.remove(user)
            groups[group].remove_user(user)
            client.close()
            break
        else:
            broadcast(bytes(message, FORMAT), user)
            print(user.name + " " + message)






def broadcast(msg, sender):
    print("broadcasting")
    
    
    for user in groups[sender.get_group()].get_people():
        client = user.conn

        try:
            client.send(bytes(sender.name + ": ", FORMAT) + msg)
        except:
            print("Message failed to send")
            client.close()
            break




if __name__ == "__main__":
    start_server(local_server)