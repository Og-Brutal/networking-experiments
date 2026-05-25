from tcp import *
from time import *

# ── poll() CONCEPT ──────────────────────────────────────────────
# Real poll() signature:
#   poll(pollfd_array, nfds, timeout_ms)
#
# pollfd structure per socket:
#   fd      -> the socket file descriptor
#   events  -> what to watch: POLLIN | POLLOUT | POLLERR
#   revents -> what actually happened (filled by kernel after poll())
#
# poll() advantage over select():
#   - No FD_SETSIZE limit (can watch thousands of fds)
#   - revents tells you EXACTLY what happened on each fd
#   - More readable: one array instead of three bit-sets

port = 12000
server = TCPServer()

# pollfd_table simulates the poll() array
# Each entry: { 'fd': ip, 'events': 'POLLIN', 'revents': '...', 'count': N }
pollfd_table = {}
clients      = {}
conn_count   = [0]

def make_poll_handler(fd_key):
    """
    Simulates poll() firing when revents = POLLIN for this fd.
    In real code this executes after poll() returns POLLIN in revents.
    """
    def on_pollin(data):
        if fd_key not in pollfd_table:
            return
        pollfd_table[fd_key]['count']   += 1
        pollfd_table[fd_key]['revents']  = 'POLLIN'
        n = str(pollfd_table[fd_key]['count'])
        print('')
        print('[ poll() ] fd=' + fd_key + ' | revents=POLLIN | msg#' + n)
        print('           data: ' + data)
        clients[fd_key].send('[poll-reply fd=' + fd_key + ']: ' + data)
    return on_pollin

def onNewClient(c):
    conn_count[0] += 1
    ip  = c.remoteIP()
    key = 'fd' + str(conn_count[0]) + ':' + ip
    clients[key]     = c
    pollfd_table[key] = {
        'fd':      key,
        'events':  'POLLIN',    # we want to monitor incoming data
        'revents': 'POLLNONE',  # nothing yet
        'count':   0
    }
    c.onReceive(make_poll_handler(key))
    print('[poll] REGISTERED fd=' + key)
    print('[poll] events=POLLIN | revents=POLLNONE (waiting...)')
    print('[poll] Total fds in pollfd array: ' + str(conn_count[0]))

server.onNewClient(onNewClient)
server.listen(port)

print('poll()-style Server running on port ' + str(port))
print('pollfd array will grow as clients connect.')
print('')

# Print pollfd table snapshot every 6 seconds
tick = [0]
while True:
    sleep(1)
    tick[0] += 1
    if tick[0] % 6 == 0:
        print('')
        print('===== poll() pollfd TABLE SNAPSHOT (tick=' + str(tick[0]) + ') =====')
        for k in pollfd_table:
            e  = pollfd_table[k]
            print('  fd=' + e['fd'] +
                  ' | events=' + e['events'] +
                  ' | revents=' + e['revents'] +
                  ' | msg_count=' + str(e['count']))
        print('======================================================')
