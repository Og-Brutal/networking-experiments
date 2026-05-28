# Computer Networks Lab 13: Dynamic Routing Protocols (RIP, EIGRP & OSPF)

This repository directory contains the implementation files, topologies, and report for **Lab 13: Dynamic Routing Protocols (RIP, EIGRP & OSPF)**.

---

## 🎯 Lab Objectives
1. Understand and implement **RIP (Routing Information Protocol)** — a distance-vector protocol using hop count as a routing metric.
2. Understand and implement **EIGRP (Enhanced Interior Gateway Routing Protocol)** — Cisco's hybrid protocol using composite metrics (bandwidth, delay). 
3. Understand and implement **OSPF (Open Shortest Path First)** — a link-state protocol using Dijkstra's SPF algorithm.
4. Design VLSM-based subnets for OSPF topology to accommodate variable host requirements (4000, 3000, 2500, 1800 hosts).
5. Verify dynamic routing convergence using ping tests across multi-router topologies. 

---

## 💻 Lab Files
| File | Description |
| :--- | :--- |
| `Lab 13 week 13 CL3001 .docx` | Official lab manual |
| `cn_lab_13_01.pkt` | Cisco Packet Tracer — Task 1 (RIP) topology |
| `cn_lab_13_02.pkt` | Cisco Packet Tracer — Task 2 (EIGRP) topology |
| `cn_lab_13_03.pkt` | Cisco Packet Tracer — Task 3 (OSPF) topology |
| `cn_lab_13_04.pkt` | Cisco Packet Tracer — Additional OSPF variant |
| `23F3043_CN_LAB#13.docx` | Premium styled lab report |

---

## ✍️ Task 1: RIP Protocol

### Network Topology
Three routers (Router0, Router1, Router2) interconnected via serial links. Each router serves a local LAN with 2 PCs.

### IP Addressing Table
| Device | Interface | IP Address | Subnet | Subnet Mask |
| :--- | :--- | :--- | :--- | :--- |
| Router0 (Left) | Se2/0 | 10.0.0.1 | 10.0.0.0/30 | 255.255.255.252 |
| Router0 (Left) | Fa0/0 | 192.168.10.1 | 192.168.10.0/24 | 255.255.255.0 |
| Router1 (Middle) | Se2/0 | 10.0.0.2 | 10.0.0.0/30 | 255.255.255.252 |
| Router1 (Middle) | Se3/0 | 11.0.0.1 | 11.0.0.0/30 | 255.255.255.252 |
| Router1 (Middle) | Fa0/0 | 192.168.20.1 | 192.168.20.0/24 | 255.255.255.0 |
| Router2 (Right) | Se2/0 | 11.0.0.2 | 11.0.0.0/30 | 255.255.255.252 |
| Router2 (Right) | Fa0/0 | 192.168.30.1 | 192.168.30.0/24 | 255.255.255.0 |

### RIP Configuration
```ios
router rip
version 2
no auto-summary
network 10.0.0.0
network 11.0.0.0
network 192.168.10.0
network 192.168.20.0
network 192.168.30.0
```

---

## ✍️ Task 2: EIGRP Protocol

### Network Topology
An 8-router ring structure (R0-R7) with two internal cross-links (R3-R4, R4-R5), a PC-side LAN (via R3) and a Server-side LAN (via R5). Autonomous System number: 100.

### EIGRP Configuration
```ios
enable
conf t
router eigrp 100
no auto-summary
network 192.168.0.0
network 192.168.1.0
network 192.168.2.0
network 10.0.0.0
network 20.0.0.0
```

---

## ✍️ Task 3: OSPF with VLSM

### VLSM LAN Subnet Allocation
| Purpose | Network | Mask |
| :--- | :--- | :--- |
| LAN (4000 hosts) | 100.0.0.0/20 | 255.255.240.0 |
| LAN (3000 hosts) | 100.0.16.0/20 | 255.255.240.0 |
| LAN (2500 hosts) | 100.0.32.0/20 | 255.255.240.0 |
| LAN (1800 hosts) | 100.0.48.0/21 | 255.255.248.0 |

### WAN Serial Link Subnets
| Link | Network | IPs |
| :--- | :--- | :--- |
| R0–R1 | 100.0.56.0/30 | .1 / .2 |
| R0–R2 | 100.0.56.4/30 | .5 / .6 |
| R1–R3 | 100.0.56.8/30 | .9 / .10 |
| R2–R3 | 100.0.56.12/30 | .13 / .14 |

### OSPF Configuration
```ios
router ospf 1
network 100.0.0.0 0.255.255.255 area 0
```

---

## 📊 Protocol Comparison

| Feature | RIP | EIGRP | OSPF |
| :--- | :--- | :--- | :--- |
| **Type** | Distance-Vector | Hybrid (Advanced DV) | Link-State |
| **Metric** | Hop Count (max 15) | Composite (BW + Delay) | Cost (based on BW) |
| **Algorithm** | Bellman-Ford | DUAL | Dijkstra SPF |
| **Convergence** | Slow | Fast | Fast |
| **VLSM Support** | v2 only | Yes | Yes |
| **Scalability** | Small networks | Medium-Large | Large enterprise |
| **Standard** | Open (RFC 2453) | Cisco Proprietary | Open (RFC 2328) |

---

## 📈 Verification Tests
- **Task 1 (RIP)**: Successful pings across all 3 LANs (192.168.10.x ↔ 192.168.20.x ↔ 192.168.30.x).
- **Task 2 (EIGRP)**: PC (10.0.0.2) successfully pings Server (20.0.0.2) across the 8-router ring topology.
- **Task 3 (OSPF)**: All subnets (100.0.0.0/20, 100.0.16.0/20, etc.) are reachable via OSPF dynamic routing.
