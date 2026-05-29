# Computer Networks — Lab 10: Persistent Connections & Concurrent Servers

## Overview
This lab covers the design, implementation, and analysis of **Persistent Connections** and **Concurrent Servers** using Python socket programming in Cisco Packet Tracer. Sockets that persist over multiple transmissions (persistent) and handle multiple clients simultaneously (concurrent) are fundamental building blocks of modern network applications (e.g., HTTP/1.1+, database streams, multiplayer online games, and chat systems). This lab implements both TCP-based and UDP-based persistent and concurrent communication, verifying PDU structures and Layer 4 states in  Simulation Mode. 

## Objectives
*   Configure a virtual subnet in Cisco Packet Tracer including PC clients, a server, and a switch.
*   Implement a **Persistent TCP Server** and Client that sustains communication over multiple messages within a single TCP session.
*   Implement a **Persistent UDP Server** and Client that handles successive datagrams without state-setup overhead.
*   Demonstrate server **concurrency** by running multiple PC clients (PC0 and PC1) concurrently, demonstrating interleaving processing on the server.
*   Trace **TCP 3-Way Handshakes** (SYN, SYN-ACK, ACK), ACK packets, Sequence/Acknowledgment numbering, and port allocation using Packet Tracer's Simulation Mode.

## Included Files 

| File | Description |
|------|-------------|
| `tcp_server.py` | TCP Server — listens on port 12000, handles persistent client connections, and echoes back replies concurrently |
| `tcp_client.py` | TCP Client — connects to port 12000, establishes connection, sends sequential payload messages, and prints replies |
| `udp_server.py` | UDP Server — binds to port 12001, logs incoming stateless datagrams, and replies to individual clients |
| `udp_client.py` | UDP Client — binds to port 12002, transmits sequential datagrams, and logs responses |
| `23F3043_CN_LAB#10.docx` | Premium, professionally styled lab report with styled code blocks, analytical Q&As, and 26 annotated figures |
| `Lab 10 week 10 .docx` | Original lab manual / instruction document |
| `CN_LAB10.pkt` | Cisco Packet Tracer topology and workspace configuration |

## How to Set Up & Run in Cisco Packet Tracer

1.  **Workspace & Topology:**
    *   Open `CN_LAB10.pkt` in Cisco Packet Tracer.
    *   Topology: PC0 (`192.168.1.1`), PC1 (`192.168.1.3`), and Server (`192.168.1.2`) connected to a Layer 2 Switch.
    *   Verify static IP assignment and run ping from terminal to verify subnet connectivity.

2.  **TCP Sockets Execution:**
    *   On the Server's **Programming** tab, load `tcp_server.py` and click **Run**.
    *   On PC0 and PC1's **Programming** tabs, load `tcp_client.py` and click **Run**.
    *   The server will print `"Client connected"` for each workstation, receive their individual payloads, and reply concurrently.

3.  **UDP Sockets Execution:**
    *   Stop the TCP scripts. On the Server's **Programming** tab, load `udp_server.py` and click **Run**.
    *   On PC0 and PC1's **Programming** tabs, load `udp_client.py` and click **Run**.
    *   The client nodes will transmit datagrams independently. The server logs the messages and uses the extracted source IP/port to reply.

4.  **Simulation & OSI Layer 4 Analysis:**
    *   Switch to **Simulation Mode** (bottom right).
    *   Trace the exchange of control packets (SYN, SYN-ACK, ACK) during TCP handshake.
    *   Inspect Layer 4 headers in the PDU Detail windows to compare TCP stream sequence parameters against UDP stateless datagram attributes.

## Key Theoretical Concepts
*   **Persistent vs. Non-Persistent:** In non-persistent sockets, the channel closes after one message, incurring connection-setup latency for every single request. In persistent connections, the channel is kept open, allowing multiple sequential messages to share the same session.
*   **Concurrency:** Concurrent servers process requests from multiple clients at the same time. The TCP server achieves this using separate client tracking sockets (triggered via `onNewClient`), while the UDP server naturally handles concurrent datagrams using the stateless, source-routed nature of UDP packets (identifying distinct clients using their unique IP and Port 4-tuple).
*   **Reliability:** TCP ensures reliable transmission via sequence numbers, acknowledgment matching, and automatic packet retransmission on loss. UDP is connectionless and unreliable, providing faster, low-overhead, best-effort packet delivery.

## Notes
*   This directory is optimized specifically for Cisco Packet Tracer simulations using its custom Python Skulpt dialect.
*   Open the `.docx` report with Microsoft Word or LibreOffice for full premium formatting.
