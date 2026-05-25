# Lab 11: Advanced Socket Options & Multiplexing (select/poll)

This directory contains the source code, Packet Tracer simulation model, lab manual, and the premium styled solution report for **Computer Networks Lab 11 (Advanced Socket Options & Multiplexing)**.

---

## 1. Objectives & Overview

In this lab, we analyze how enterprise-scale networking applications tune socket behaviors and handle thousands of simultaneous client connections efficiently. The lab is divided into three key socket paradigms:

1. **Socket Options (`getsockopt` & `setsockopt`)**: Reading and writing internal socket settings such as address reuse flags (`SO_REUSEADDR`) to avoid TIME_WAIT socket locks, and connection blocking receive timeouts (`SO_RCVTIMEO`).
2. **Synchronous I/O Multiplexing (`select`)**: Monitoring multiple socket descriptors simultaneously within a single thread up to `FD_SETSIZE` (usually 1024).
3. **Scalable Multiplexing (`poll`)**: An advanced descriptor multiplexer using an array of `pollfd` structures that bypasses `FD_SETSIZE` limits and simplifies event flags for high-concurrency environments.

---

## 2. File Directory Structure

```text
computer_networks_lab_11/
├── 23F3043_CN_LAB#11.docx         # Premium, professionally formatted solution report
├── Lab 11 week 11 CL3001 .docx    # Original lab manual and questions sheet
├── cn_lab_11.pkt                 # Cisco Packet Tracer network simulation topology
├── README.md                     # Overview, file listings, and simulation guide
│
├── setsockopt_server.py          # Part A: TCP Socket options demonstration server
├── setsockopt_client.py          # Part A: TCP Socket options demonstration client (PC-A)
│
├── select_server.py              # Part B: select() synchronous multiplexing TCP server
├── select_client_a.py            # Part B: select() client script (PC-A)
├── select_client_b.py            # Part B: select() client script (PC-B)
│
├── poll_server.py                # Part C: poll() event-driven multiplexing TCP server
├── poll_client_a.py              # Part C: poll() client script (PC-A)
├── poll_client_b.py              # Part C: poll() client script (PC-B)
└── poll_client_c.py              # Part C: poll() client script (PC-C)
```

---

## 3. Cisco Packet Tracer Physical Setup

Before executing any script, configure the subnet topology using the provided `cn_lab_11.pkt` simulation:
- **Central Server0**: `192.168.1.10` (acts as DNS, HTTP, and FTP host)
- **Workstation PC-A**: `192.168.1.1` (DNS Server: `192.168.1.10`)
- **Workstation PC-B**: `192.168.1.2` (DNS Server: `192.168.1.10`)
- **Workstation PC-C**: `192.168.1.3` (DNS Server: `192.168.1.10`)

All nodes are interconnected through Copper Straight-Through cables via a central Layer-2 Switch.

---

## 4. Run & Simulation Instructions

### Part A: setsockopt() & getsockopt()
1. Run `setsockopt_server.py` on **Server0**'s programming tab. It will output getsockopt read-back option parameters:
   - `SO_REUSEADDR = 1`
   - `SO_RCVTIMEO = 8 seconds`
2. Run `setsockopt_client.py` on **PC-A**. It will read back dynamic options, connect, and transmit two periodic test messages.
3. Switch to **Simulation Mode** (edit filters: `TCP`, `HTTP`) to inspect the TCP outbound headers and flow-control window dynamics.

### Part B: select() Multiplexing
1. Run `select_server.py` on **Server0**'s programming tab to monitor `read_fds`.
2. Run `select_client_a.py` on **PC-A** and `select_client_b.py` on **PC-B**.
3. Observe how a single thread on Server0 multiplexes both incoming client connections simultaneously, printing interleaved `fd_label` dispatch logs.

### Part C: poll() Scalable Multiplexing
1. Run `poll_server.py` on **Server0** to register and dynamically scale the `pollfd` structures.
2. Run `poll_client_a.py` on **PC-A**, `poll_client_b.py` on **PC-B**, and `poll_client_c.py` on **PC-C**.
3. The server prints live array snapshots demonstrating efficient `revents = POLLIN` state routing.

---

## 5. Comparative Multiplexing Analysis

| Metric / Feature | `select()` | `poll()` |
| :--- | :--- | :--- |
| **Max Connections** | Fixed `FD_SETSIZE` (usually 1024) | Unlimited (scales dynamically with memory) |
| **Data Structure** | Bit-mask sets (`read_fds`, `write_fds`, `error_fds`) | Array of `pollfd` structs (`fd`, `events`, `revents`) |
| **Performance Overhead** | $O(N)$ — requires scanning all descriptors up to max | $O(N)$ — scan of active array elements |
| **Descriptor Reusability** | Modifies the mask; must re-initialize every loop | Segregates input (`events`) & output (`revents`); reusable |
| **Scale Suitability** | Small scale / Legacy systems | Medium scale / Multi-service servers |
