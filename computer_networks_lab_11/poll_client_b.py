from tcp import *
from time import *

serverIP = '192.168.1.10'  # Corrected from 192.168.1.2 in manual to connect to Server0
port     = 12000
client   = TCPClient()
ready    = [False]

def onReceive(data): print('[PC-B] ' + data)

def onConnect(t):
    if t == 0: ready[0] = True

client.onReceive(onReceive)
client.onConnectionChange(onConnect)
client.connect(serverIP, port)

count = 0
while not ready[0] and count < 15:
    sleep(1); count += 1

if ready[0]:
    sleep(3)
    client.send('PC-B POLLIN trigger 1')
    sleep(2)
    client.send('PC-B POLLIN trigger 2')
    sleep(2)
    print('PC-B done.')
