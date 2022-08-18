from client import Client
import time

c1 = Client('test1', 'test')
time.sleep(5)
c2 = Client('test2', 'test')
time.sleep(5)
c3 = Client('test3', 'test_group')
time.sleep(5)
c4 = Client('test4', 'test_group')
time.sleep(5)
c1.send_message("#DISCONNECT")
#c1.send_message('hi')
#time.sleep(5)
#c2.send_message('whats up')
#time.sleep(5)
#c1.send_message("#DISCONNECT")
#time.sleep(5)
#c2.send_message("#DISCONNECT")