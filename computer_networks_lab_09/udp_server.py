from udp import *
from time import *

def onUDPReceive(ip, port, data):
	print("received from " + ip + ":" + str(port) + " -> " + data)

def main():
	socket = UDPSocket()
	socket.onReceive(onUDPReceive)

	print(socket.begin(12001))

	while True:
		sleep(3600)

if __name__ == "__main__":
	main()
