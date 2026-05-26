# Computer Networks Lab 12: IP Subnetting & Static Routing (FLSM & VLSM)

This repository directory contains the implementation files, topologies, calculations, and screenshots for **Lab 12: IP Subnetting & Static Routing (FLSM & VLSM)**.

---

## 🎯 Lab Objectives
1. Understand **Fixed Length Subnet Masking (FLSM)** and perform address subnetting for Class A, B, and C networks.
2. Understand **Variable Length Subnet Masking (VLSM)** and design subnets optimized for variable host counts (2000, 1000, 400, and 2 hosts) to minimize address wastage.
3. Configure interfaces on Cisco Routers and End Devices in Cisco Packet Tracer.
4. Establish static routing pathways across multiple subnets.
5. Verify bidirectional network convergence using end-to-end ping tests.

---

## 💻 Lab Files
- **[`Lab 12 week 12 CL3001 .docx`](file:///e:/Random_Projects/networking-experiments/computer_networks_lab_12/Lab%2012%20week%2012%20CL3001%20.docx)**: The official lab manual.
- **[`cn_lab_12.pkt`](file:///e:/Random_Projects/networking-experiments/computer_networks_lab_12/cn_lab_12.pkt)**: Cisco Packet Tracer network simulation file containing both FLSM and VLSM topology scenarios.
- **[`23F3043_CN_LAB#12.docx`](file:///e:/Random_Projects/networking-experiments/computer_networks_lab_12/23F3043_CN_LAB#12.docx)**: The final premium lab report with custom typography, table grids, and embedded Packet Tracer screenshots.

---

## ✍️ Subnetting Calculations

### 1. FLSM Subnetting Designs

#### IP = 100.0.0.0 for 3000 subnets
- **Class**: Class A (Default Mask: /8)
- **Subnet bits needed**: $2^{12} = 4096 \ge 3000$ (Borrow 12 bits)
- **New Subnet Mask**: /20 (255.255.240.0)
- **Block Size (Increment)**: 16 (in 3rd octet)
- **Subnet Table (First 2 subnets)**:
  | Subnet No. | Subnet ID | Subnet Mask | 1st Usable IP | Last Usable IP | Broadcast IP |
  | :--- | :--- | :--- | :--- | :--- | :--- |
  | **Subnet 1** | 100.0.0.0 | 255.255.240.0 | 100.0.0.1 | 100.0.15.254 | 100.0.15.255 |
  | **Subnet 2** | 100.0.16.0 | 255.255.240.0 | 100.0.16.1 | 100.0.31.254 | 100.0.31.255 |

#### IP = 150.89.0.0 for 1800 subnets
- **Class**: Class B (Default Mask: /16)
- **Subnet bits needed**: $2^{11} = 2048 \ge 1800$ (Borrow 11 bits)
- **New Subnet Mask**: /27 (255.255.255.224)
- **Block Size (Increment)**: 32 (in 4th octet)
- **Subnet Table (First 2 subnets)**:
  | Subnet No. | Subnet ID | Subnet Mask | 1st Usable IP | Last Usable IP | Broadcast IP |
  | :--- | :--- | :--- | :--- | :--- | :--- |
  | **Subnet 1** | 150.89.0.0 | 255.255.255.224 | 150.89.0.1 | 150.89.0.30 | 150.89.0.31 |
  | **Subnet 2** | 150.89.0.32 | 255.255.255.224 | 150.89.0.33 | 150.89.0.62 | 150.89.0.63 |

#### IP = 203.45.67.0 for 10 subnets
- **Class**: Class C (Default Mask: /24)
- **Subnet bits needed**: $2^4 = 16 \ge 10$ (Borrow 4 bits)
- **New Subnet Mask**: /28 (255.255.255.240)
- **Block Size (Increment)**: 16 (in 4th octet)
- **Subnet Table (First 2 subnets)**:
  | Subnet No. | Subnet ID | Subnet Mask | 1st Usable IP | Last Usable IP | Broadcast IP |
  | :--- | :--- | :--- | :--- | :--- | :--- |
  | **Subnet 1** | 203.45.67.0 | 255.255.255.240 | 203.45.67.1 | 203.45.67.14 | 203.45.67.15 |
  | **Subnet 2** | 203.45.67.16 | 255.255.255.240 | 203.45.67.17 | 203.45.67.30 | 203.45.67.31 |
