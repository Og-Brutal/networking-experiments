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
