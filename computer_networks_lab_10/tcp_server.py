from tcp import *
from time import *

port = 12000
server = TCPServer()
message_count = 0

def onTCPNewClient(client):
    print("Client connected: " + client.remoteIP())
    def onTCPReceive(data):
        global message_count
        message_count = message_count + 1
        print("Message " + str(message_count) + " received: " + data)
        client.send("Server reply " + str(message_count) + ": Got your message!")
    def onTCPConnectionChange(type):
        if type == 0:
            print("Client disconnected: " + client.remoteIP())
    client.onReceive(onTCPReceive)
    client.onConnectionChange(onTCPConnectionChange)

server.onNewClient(onTCPNewClient)
server.listen(port)
print("Persistent TCP Server listening on port 12000...")

while True:
    sleep(1)
