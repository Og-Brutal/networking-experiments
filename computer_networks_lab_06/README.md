# Computer Networks — Lab 07: Socket Programming Part II

## Overview
This lab explores **TCP** and **UDP** client-server communication using the POSIX socket API in C++. Both connection-oriented (TCP) and connectionless (UDP) paradigms are implemented and tested on `localhost:8080`.

## Objectives
*   Implement a TCP client-server pair using `socket()`, `bind()`, `listen()`, `accept()`, `connect()`, `send()`, and `read()`.
*   Implement a UDP client-server pair using `socket()`, `bind()`, `sendto()`, and `recvfrom()`.
*   Observe and compare the behavioral differences between TCP and UDP communication.
*   Understand the role of `sockaddr_in` structures, port binding, and address families (`AF_INET`).

## Included Files

| File | Description |
|------|-------------|
| `tcp_client.cpp` | TCP client — connects to server and sends a greeting |
| `tcp_server.cpp` | TCP server — listens on port 8080, accepts a connection, echoes a reply |
| `udp_client.cpp` | UDP client — sends a datagram and receives the server's response |
| `udp_server.cpp` | UDP server — binds to port 8080, receives a datagram, sends a reply |
| `23F3043_cn_lab_07.docx` | Lab solution report with code listings and terminal output |
| `Lab_7-Socket Pogramming Part-II.pptx` | Lab manual / reference slides |

## How to Compile & Run

### TCP
```bash
g++ tcp_server.cpp -o tcp_server
g++ tcp_client.cpp -o tcp_client

# Terminal 1
./tcp_server

# Terminal 2
./tcp_client
```

### UDP
```bash
g++ udp_server.cpp -o udp_server
g++ udp_client.cpp -o udp_client

# Terminal 1
./udp_server

# Terminal 2
./udp_client
```

## Key Concepts
*   **TCP (SOCK_STREAM):** Reliable, connection-oriented — guarantees ordered delivery via a 3-way handshake.
*   **UDP (SOCK_DGRAM):** Lightweight, connectionless — best-effort delivery with no connection overhead.
*   **Port 8080:** Both implementations bind to this port on `127.0.0.1` (loopback).

## Notes
*   All programs are written for Linux/POSIX environments and require `<arpa/inet.h>`, `<unistd.h>`.
*   Open the `.docx` report with Microsoft Word or LibreOffice for full formatting.
