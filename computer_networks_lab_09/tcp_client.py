from tcp import *
from time import *

serverIP = "192.168.1.2"
serverPort = 1234
client = TCPClient()

def onTCPConnectionChange(type):
	print("connection to " + client.remoteIP() + " changed to state " + str(type))

def onTCPReceive(data):
	print("received from " + client.remoteIP() + " with data: " + data)

def main():
	client.onConnectionChange(onTCPConnectionChange)
	client.onReceive(onTCPReceive)
	print(client.connect(serverIP, serverPort))
	count = 0
	while True:
		count += 1
		data = "hello " + str(count)
		client.send(data)
		sleep(5)

if __name__ == "__main__":
	main()
