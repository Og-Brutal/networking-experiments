from udp import *
from time import *

serverIP = "192.168.1.2"
serverPort = 12001

def onUDPReceive(ip, port, data):
	print("reply from " + ip + ":" + str(port) + " -> " + data)

def main():
	socket = UDPSocket()
	socket.onReceive(onUDPReceive)

	print(socket.begin(1234))   # client uses different port

	count = 0
	while True:
		count += 1
		socket.send(serverIP, serverPort, "hello " + str(count))
		sleep(2)

if __name__ == "__main__":
	main()
