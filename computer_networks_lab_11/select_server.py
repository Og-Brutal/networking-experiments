from tcp import *
from time import *

# ── select() SIMULATION ──────────────────────────────────────────
# In a real OS, select() watches multiple file descriptors (fds).
# Each onReceive() callback here fires when a socket enters read_fds.
# select_log tracks which fd became ready and when.
port       = 12000
server     = TCPServer()
select_log = []          # tracks which fd became ready
clients    = {}          # fd_label -> client object
conn_count = [0]

def make_select_handler(fd_label):
    """
    Returns an onReceive callback that logs the select() event.
    In a real select() loop, this fires when fd is in read_fds.
    """
    def on_ready(data):
        event_num = len(select_log) + 1
        select_log.append(fd_label)
        print('')
        print('=== select() returned: fd=' + fd_label + ' is in read_fds ===')
        print('    Event #' + str(event_num) + '  |  Data: ' + data)
        print('    -> Dispatching handler for ' + fd_label)
        clients[fd_label].send('[select-reply to ' + fd_label + ']: ' + data)
    return on_ready

def onNewClient(c):
    conn_count[0] += 1
    label = 'fd' + str(conn_count[0]) + '_' + c.remoteIP()
    clients[label] = c
    c.onReceive(make_select_handler(label))
    print('[select] New fd registered: ' + label)
    print('[select] Total fds in read_fds set: ' + str(conn_count[0]))

server.onNewClient(onNewClient)
server.listen(port)

print('select()-style Server ready on port ' + str(port))
print('Monitoring read_fds | write_fds | error_fds...')
print('Waiting for clients to appear in read_fds...')
print('')

# Polling loop simulates select() blocking with a 1s timeout
tick = [0]
while True:
    sleep(1)
    tick[0] += 1
    if tick[0] % 5 == 0:
        print('[select timeout] tick=' + str(tick[0]) +
              ' | total events so far: ' + str(len(select_log)))
