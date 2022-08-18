import socket
import threading
import time



class Client:

    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 5050
    ADDR = (HOST, PORT)
    BUFSIZE = 512
    DISCONNECT_MESSAGE = "#DISCONNECT"
    FORMAT = "utf8"

    
    def __init__(self, name, group):
        self.name = name
        self.group = group
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(self.ADDR)
        self.messages = []
        get_thread = threading.Thread(target=self.get_messages)
        get_thread.start()
        self.send_message(name)
        time.sleep(5)
        self.send_message(group)

        self.lock = threading.Lock()


    def get_messages(self):
        
        while True:
            try:
                message = self.client_socket.recv(self.BUFSIZE).decode(self.FORMAT)
                if message == f"Unable to join, {self.group} is currently at capacity":
                    self.client_socket.close()
                    
                else:
                    self.lock.acquire()
                    if len(message) != 0:
                        print(message)
                        self.messages.append(message)
                        #print(self.messages)
                    else:
                        self.client_socket.close()
                    self.lock.release()
                
            except:
                print("Error")
                break


    def send_message(self, message):
        print("sending message")
        try:
            self.client_socket.send(bytes(message, self.FORMAT))
            print("message sent")
            if message == self.DISCONNECT_MESSAGE:
                time.sleep(10)
                self.client_socket.close()
        except:
            print("Message error")
            

    def all_messages(self):
        return self.messages