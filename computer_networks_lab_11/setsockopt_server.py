from tcp import *
from time import *

# ── setsockopt() SIMULATION ─────────────────────────────────────
# PT does not expose setOption/getOption on TCPServer.
# We simulate setsockopt by storing options as plain variables.
# In a real OS: setsockopt(sock, SOL_SOCKET, SO_REUSEADDR, &1, sizeof(1))
port = 12000
server = TCPServer()

# Simulated setsockopt() calls
socket_options = {
    'SO_REUSEADDR': 1,   # allow port reuse after server restart
    'SO_RCVTIMEO':  8,   # receive timeout = 8 seconds
}

# ── getsockopt() SIMULATION ─────────────────────────────────────
# In real C: getsockopt(sock, SOL_SOCKET, SO_REUSEADDR, &val, &len)
reuse = socket_options['SO_REUSEADDR']
timeo = socket_options['SO_RCVTIMEO']

print('=== getsockopt() READ-BACK ===')
print('SO_REUSEADDR = ' + str(reuse) + '  (1=ON, 0=OFF)')
print('SO_RCVTIMEO  = ' + str(timeo) + ' seconds')
print('===============================')

# ── Server logic ─────────────────────────────────────────────────
client_ref = [None]

def onNewClient(c):
    client_ref[0] = c
    ip = c.remoteIP()
    print('')
    print('[setsockopt] New client from: ' + ip)
    print('[getsockopt] SO_REUSEADDR=' + str(reuse) + ' SO_RCVTIMEO=' + str(timeo) + 's')
    c.onReceive(onReceive)

msg_count = [0]

def onReceive(data):
    msg_count[0] += 1
    print('[Recv #' + str(msg_count[0]) + '] ' + data)
    client_ref[0].send('Echo from server: ' + data)

server.onNewClient(onNewClient)
server.listen(port)

print('Server listening on port ' + str(port) + '...')
print('SO_REUSEADDR lets this server restart on the same port immediately.')

while True:
    sleep(1)
