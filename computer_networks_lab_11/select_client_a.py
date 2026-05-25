from tcp import *
from time import *

serverIP = '192.168.1.10'
port     = 12000
client   = TCPClient()
ready    = [False]

def onReceive(data):
    print('[PC-A select-reply]: ' + data)

def onConnect(t):
    if t == 0: ready[0] = True

client.onReceive(onReceive)
client.onConnectionChange(onConnect)
client.connect(serverIP, port)

count = 0
while not ready[0] and count < 15:
    sleep(1); count += 1

if ready[0]:
    sleep(1)
    # This message enters the server's read_fds set -> select() fires
    client.send('PC-A: Message-1 entering select read_fds')
    sleep(4)   # delay so PC-B can also connect and both appear in read_fds
    client.send('PC-A: Message-2 entering select read_fds')
    sleep(2)
    print('PC-A done.')
