from tcp import *
from time import *

serverIP = '192.168.1.2'
port = 12000
client = TCPClient()

# Use list instead of global variable - Skulpt handles list mutation in callbacks
isConnected = [False]

def onReceive(data):
    print("Server replied: " + data)

def onConnectionChange(type):
    if type == 0:
        isConnected[0] = True
        print("Connected to server!")
    if type == 1:
        print("Disconnected from server.")

client.onReceive(onReceive)
client.onConnectionChange(onConnectionChange)
client.connect(serverIP, port)
print("Connecting...")

# Wait until callback confirms connection
count = 0
while not isConnected[0] and count < 20:
    sleep(1)
    count = count + 1

if isConnected[0]:
    sleep(2)
    print("Sending Message 1...")
    client.send("Hello from Client! Message 1")
    sleep(3)
    print("Sending Message 2...")
    client.send("Hello from Client! Message 2")
    sleep(3)
    print("Sending Message 3...")
    client.send("Hello from Client! Message 3")
    sleep(3)
    print("All messages sent. Done.")
    sleep(2)
else:
    print("Connection failed.")
