from udp import *
from time import *

message_count = 0

def onUDPReceive(ip, port, data):
    global message_count
    message_count = message_count + 1
    print("UDP Message " + str(message_count) + " from " + ip + ": " + data)
    socket.send(ip, port, "UDP Reply " + str(message_count) + ": Received!")

def main():
    global socket
    socket = UDPSocket()
    socket.onReceive(onUDPReceive)
    print(socket.begin(12001))
    print("UDP Server listening on port 12001...")
    while True:
        sleep(1)

if __name__ == "__main__":
    main()
