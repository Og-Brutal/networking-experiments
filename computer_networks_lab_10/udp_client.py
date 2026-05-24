from udp import *
from time import *

def onUDPReceive(ip, port, data):
    print("Server replied: " + data)

def main():
    socket = UDPSocket()
    socket.onReceive(onUDPReceive)
    socket.begin(12002)
    print("UDP Client ready...")
    sleep(2)
    print("Sending UDP Message 1...")
    socket.send("192.168.1.2", 12001, "UDP Hello! Message 1")
    sleep(2)
    print("Sending UDP Message 2...")
    socket.send("192.168.1.2", 12001, "UDP Hello! Message 2")
    sleep(2)
    print("Sending UDP Message 3...")
    socket.send("192.168.1.2", 12001, "UDP Hello! Message 3")
    sleep(2)
    print("All UDP messages sent. Done.")

if __name__ == "__main__":
    main()
