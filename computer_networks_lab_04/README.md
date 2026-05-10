# Hierarchical Network Topology — Static Routing & Connectivity

**Course:** CL3001 - Computer Networks  
**Lab:** 05 | Week 5  
**Campus:** National University of Computer & Emerging Sciences, Chiniot-Faisalabad  
**Instructor:** Esha Iftikhar  

---

## Overview

This lab focuses on building a complete hierarchical network topology in Cisco Packet Tracer featuring one main router (R1), four branch routers (B1–B4 using 2621XM), switches per branch, and an ISP connection. Tasks 1 & 2 together cover the entire workflow — from designing the IP addressing scheme and physically cabling devices, to configuring IP addresses on every interface and verifying end-to-end connectivity.

---

## Objectives

- Design and document an addressing scheme based on network requirements
- Select appropriate equipment (2621XM routers, 2960-24TT switches) and cable the devices correctly
- Apply basic configuration to all devices via Config tab and CLI
- Configure static and default routing so all routers can communicate
- Verify full connectivity between all devices using ping commands from the CLI

---

## Network Architecture

```
                        ┌──────────┐
                        │  2621XM  │
                        │    B4    │
                        └────┬─────┘
                             │ Serial (WAN)
                             │
    ┌──────────┐        ┌────┴─────┐        ┌──────────┐
    │  2621XM  │ Serial │  2621XM  │ Serial │  2621XM  │
    │    B1    ├────────┤    R1    ├────────┤    B3    │
    └────┬─────┘  (WAN) └────┬─────┘  (WAN) └────┬─────┘
         │                   │                     │
    ┌────┴────┐              │ Serial (WAN)   ┌────┴────┐
    │ B1_S3/4 │              │                │ B3_S3/4 │
    │ Switches│         ┌────┴─────┐          │ Switches│
    └─────────┘         │  2621XM  │          └─────────┘
                        │    B2    │
                        └────┬─────┘
                        ┌────┴────┐
                        │ B2_S3/4 │
                        │ Switches│
                        └─────────┘
```

### Addressing Scheme

| Subnet Purpose | Network Address | Subnet Mask |
|---|---|---|
| WAN Links (R1 ↔ Branches) | 10.0.1.0/28 (split into /30 subnets) | 255.255.255.252 |
| LAN Subnets (Branch LANs) | 10.1.0.0/16 (split into /18 then /20) | Varies per branch |

---

## Solution Screenshots

The solution PDF contains 5 annotated screenshots documenting the entire configuration process:

| # | Screenshot | Description |
|---|---|---|
| 1 | Packet Tracer Topology (Cabling Stage) | Initial workspace after all routers and switches are placed and physically cabled — red serial links indicate WAN connections are not yet configured |
| 2 | Router B1 Config Tab (IP Assignment) | Config tab of Branch Router B1 showing FastEthernet0/0 with IP 10.1.0.0 and subnet mask 255.0.0.0 being entered via the GUI |
| 3 | Topology After Cabling (Red Links Down) | Intermediate stage — LAN links show green triangles (UP) while WAN serial links remain red (IPs not yet assigned on serial interfaces) |
| 4 | Topology After Full Configuration (Green Links Up) | Final configured topology — all serial WAN links display green triangle indicators confirming full IP configuration and DCE clock rate set |
| 5 | Router R1 CLI (IP & Ping Verification) | R1 CLI tab showing serial interface IP configuration commands and a successful ping to 1.0.0.1 with 100% success rate (5/5 packets) |

---

## Concepts Demonstrated

```
OSI Layers Applied
------------------
Layer 3  Network        IP addressing (/30 WAN, /20 LAN) / Static & Default Routing
Layer 2  Data Link      Ethernet (switch to router) / Serial (WAN point-to-point)
Layer 1  Physical       DCE/DTE cabling / Clock rate configuration / WIC-2T module
```

| Concept | What Was Learned |
|---|---|
| Subnetting | 10.0.1.0/28 split into /30 WAN subnets; 10.1.0.0/16 split into /18 then /20 LAN subnets |
| Config Tab vs CLI | Both methods achieve the same result — GUI auto-generates equivalent IOS commands |
| DCE/DTE | R1 is DCE on all WAN links; must set clock rate 64000 for serial links to come up |
| Link Status Indicators | Red = down/unconfigured; Green triangle = Layer 1 + Layer 2 both UP |
| Ping Testing | Confirms Layer 3 reachability; !!!!! = 100% success; . = timeout/failure |
| Static Routing | Manually defined routes enable inter-branch communication through R1 |

---

## Repository Structure

```
computer_networks_lab_04/
│
├── README.md                           <- This file
├── CN_Lab05_Solution_Explained.pdf     <- Full professional lab report with annotated screenshots
└── Lab 5 week 5  (1).docx             <- Lab manual provided by instructor
```
