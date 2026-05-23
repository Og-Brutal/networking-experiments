# Computer Networks — Lab 09: Socket Programming in Cisco Packet Tracer

## Overview
This lab explores basic network programming concepts, the OSI model, socket APIs, and TCP/UDP client-server communication using **Cisco Packet Tracer**. Using Packet Tracer's internal Python programming environment, we implemented both a connection-oriented (TCP) echo service and a connectionless (UDP) message exchange service. We then monitored active listening ports via the virtual terminal and visualized transport layer handshakes and protocol encapsulation through Packet Tracer's Simulation Mode.

## Objectives
*   Configure a network topology in Cisco Packet Tracer simulating client-server interactions.
*   Implement standard client-server socket scripts using Cisco Packet Tracer's built-in Python environment.
*   Monitor active ports, listening states, and network statistics using the `netstat` command.
*   Analyze the **TCP 3-Way Handshake** (SYN, SYN-ACK, ACK) and connection states in Simulation Mode.
*   Compare connectionless (UDP) and connection-oriented (TCP) behaviors under the 7-Layer OSI model framework.

## Included Files

| File | Description |
|------|-------------|
| `tcp_server.py` | TCP Server — binds to port 1234, listens for clients, accepts connections, and echoes back received data |
| `tcp_client.py` | TCP Client — connects to the server, transmits incremental 'hello <count>' payloads, and prints replies |
| `udp_server.py` | UDP Server — binds to port 12001, registers callbacks to receive datagram packets, and logs data |
| `udp_client.py` | UDP Client — binds to local port 1234, transmits periodic messages to server IP at port 12001 |
| `23F3043_CN_LAB#09.docx` | Premium, professionally styled lab solution report with code listings, OSI layers analysis, and annotated screenshots |
| `Lab 9 week 9  .docx` | Original lab manual / instruction document |

## How to Set Up & Run in Cisco Packet Tracer

1.  **Topology Configuration:**
    *   Place a **PC** and a **Server** in the workspace.
    *   Connect them using a **Copper Straight-Through** cable.
    *   Assign static IP addresses: PC Client (`192.168.1.1`) and Server (`192.168.1.2`).

2.  **Running the Python Sockets:**
    *   Click on the server device, navigate to the **Programming** tab, and create a new Python project.
    *   Add `tcp_server.py` or `udp_server.py` and click **Run**.
    *   Click on the client PC, navigate to its **Programming** tab, load the corresponding client script, and click **Run**.

3.  **Port Verification:**
    *   On the Server's virtual Desktop, open the **Command Prompt**.
    *   Run `netstat` to verify that port `1234` (for TCP) or `12001` (for UDP) is in a `LISTENING` state.

4.  **Simulation & OSI Analysis:**
    *   Switch to **Simulation Mode** (bottom right).
    *   Watch the TCP 3-Way Handshake packets (`SYN`, `SYN-ACK`, `ACK`) propagate in real-time.
    *   Click on the active PDU envelopes to inspect the headers across the Layer 4 (TCP segments/UDP datagrams), Layer 3 (IP packets), and Layer 2 (Ethernet frames) boundaries.

## Key Concepts
*   **TCP (SOCK_STREAM):** Reliable, stream-oriented, connection-oriented. Uses port `1234` and initiates a virtual channel via the 3-Way Handshake.
*   **UDP (SOCK_DGRAM):** Unreliable, connectionless. Uses port `12001` and transmits independent datagrams instantly without establishing connection state.
*   **Skulpt Subset:** Cisco Packet Tracer executes a subset of Python, which means the built-in socket APIs are tailored for Skulpt bindings rather than standard Python C-extension sockets.

## Notes
*   This directory is optimized specifically for Cisco Packet Tracer simulations.
*   Open the `.docx` report with Microsoft Word or LibreOffice for full premium formatting.
