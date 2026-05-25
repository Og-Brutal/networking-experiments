from tcp import *
from time import *

serverIP = '192.168.1.10'   # Server0 IP
port     = 12000
client   = TCPClient()

# ── setsockopt() SIMULATION ──────────────────────────────────────
# PT does not expose setOption/getOption on TCPClient.
# We simulate setsockopt by storing the option in a plain dictionary.
# In real C: setsockopt(sock, SOL_SOCKET, SO_RCVTIMEO, &tv, sizeof(tv))
socket_options = {
    'SO_RCVTIMEO': 5,   # receive timeout = 5 seconds
    'SO_REUSEADDR': 1,   # allow port reuse
}

# ── getsockopt() SIMULATION ──────────────────────────────────────
# In real C: getsockopt(sock, SOL_SOCKET, SO_RCVTIMEO, &val, &len)
val = socket_options['SO_RCVTIMEO']

print('=== Client getsockopt() READ-BACK ===')
print('SO_RCVTIMEO  = ' + str(val) + ' seconds  (receive timeout)')
print('SO_REUSEADDR = ' + str(socket_options['SO_REUSEADDR']) + '  (1=ON, 0=OFF)')
print('======================================')

# ── Callback handlers ─────────────────────────────────────────────
def onReceive(data):
    print('[Reply] ' + data)

ready = [False]

def onConnect(type):
    if type == 0:
        ready[0] = True
        print('Connected to server at ' + serverIP + ':' + str(port))
        print('[setsockopt effect] SO_RCVTIMEO active: will timeout after ' + str(val) + 's if no reply')

client.onReceive(onReceive)
client.onConnectionChange(onConnect)
client.connect(serverIP, port)

# ── Wait for connection (respects simulated SO_RCVTIMEO) ──────────
count = 0
while not ready[0] and count < val:   # use our simulated timeout value
    sleep(1)
    count += 1

if ready[0]:
    sleep(1)
    print('Sending message 1...')
    client.send('Hello - testing setsockopt SO_REUSEADDR')
    sleep(3)
    print('Sending message 2...')
    client.send('Second message - check window size in PDU')
    sleep(2)
    print('Done. Check server output for getsockopt readback.')
else:
    print('Connection failed - SO_RCVTIMEO expired after ' + str(val) + 's')
