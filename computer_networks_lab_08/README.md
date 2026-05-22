# Computer Networks — Lab 08: Socket Programming Part II (Calculator Application)

## Overview
This lab implements a **TCP** and **UDP** network calculator application using the POSIX socket API in C++. The client captures two integers and an arithmetic operator (`+`, `-`, `*`, `/`) from user input, serializes them in a custom structured data format, and transmits them to the server. The server processes the request using a `switch-case` statement and returns the calculated result back to the client.

## Objectives
*   Implement a connection-oriented (TCP) calculator server and client.
*   Implement a connectionless (UDP) calculator server and client.
*   Demonstrate serialization of custom data structures (`struct Data`) over network sockets.
*   Explore reliable vs. unreliable transport protocols for transactional calculator exchanges.
*   Practice port binding and address structures using `sockaddr_in`.

## Included Files

| File | Description |
|------|-------------|
| `tcp_client.cpp` | TCP client — connects to server, prompts for inputs/operator, sends request, and prints result |
| `tcp_server.cpp` | TCP server — listens on port 8080, accepts TCP connection, computes arithmetic using `switch-case`, and returns result |
| `udp_client.cpp` | UDP client — prompts for inputs/operator, sends datagram to server, and prints result |
| `udp_server.cpp` | UDP server — binds to port 8081, processes arithmetic datagram using `switch-case`, and returns result |
| `23F3043_CN_LAB#08.docx` | Premium, professionally styled lab solution report with code listings and terminal output |
| `Lab 8 week 8 .docx` | Original lab manual / reference document |

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
*   **Structured Data Over Sockets:** Demonstrates that struct structures can be cast directly and written over network streams/datagrams when aligned.
*   **TCP (SOCK_STREAM):** Reliable, stream-oriented, established connection on port `8080`.
*   **UDP (SOCK_DGRAM):** Connectionless, datagram-oriented, uses port `8081`.
*   **Switch-Case Arithmetic:** Demonstrates modular server-side processing where business logic is separated from communication logic.

## Notes
*   All programs are written for Linux/POSIX environments and require `<arpa/inet.h>`, `<unistd.h>`.
*   Open the `.docx` report with Microsoft Word or LibreOffice for full premium formatting.
