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

---

### 2. VLSM Subnetting Designs

#### IP = 10.0.0.0 (Class A)
- **Subnets ordered by Host Requirements (Highest to Lowest)**:
  1. **Right LAN (2000 hosts)**: Requires $2^{11} = 2048$ addresses.
     - **Subnet Mask**: /21 (255.255.248.0)
     - **Range**: 10.0.0.0 - 10.0.7.255 (Usable: 10.0.0.1 to 10.0.7.254)
  2. **Left LAN (1000 hosts)**: Requires $2^{10} = 1024$ addresses.
     - **Subnet Mask**: /22 (255.255.252.0)
     - **Range**: 10.0.8.0 - 10.0.11.255 (Usable: 10.0.8.1 to 10.0.11.254)
  3. **Middle LAN (400 hosts)**: Requires $2^9 = 512$ addresses.
     - **Subnet Mask**: /23 (255.255.254.0)
     - **Range**: 10.0.12.0 - 10.0.13.255 (Usable: 10.0.12.1 to 10.0.13.254)
  4. **WAN Link (2 hosts)**: Requires $2^2 = 4$ addresses.
     - **Subnet Mask**: /30 (255.255.255.252)
     - **Range**: 10.0.14.0 - 10.0.14.3 (Usable: 10.0.14.1 to 10.0.14.2)

---

## 🛠️ Cisco Router Interface & Static Routing Commands

### 1. Task 1 (FLSM Topology Routing)
- **Router 1 Interfaces (Router 4)**:
  ```ios
  interface FastEthernet0/0
   ip address 196.10.0.1 255.255.255.224
   no shutdown
  interface Serial2/0
   ip address 196.10.0.97 255.255.255.224
   no shutdown
  ```
- **Router 2 Interfaces (Router 5)**:
  ```ios
  interface FastEthernet0/0
   ip address 196.10.0.65 255.255.255.224
   no shutdown
  interface Serial2/0
   ip address 196.10.0.98 255.255.255.224
   no shutdown
  ```
- **Static Route Configurations**:
  - **Router 1**: `ip route 196.10.0.64 255.255.255.224 196.10.0.98`
  - **Router 2**: `ip route 196.10.0.0 255.255.255.224 196.10.0.97`

### 2. Task 2 (VLSM Topology Routing)
- **Router 1 (Router 4)**:
  ```ios
  interface FastEthernet0/0
   ip address 10.0.8.1 255.255.252.0
   no shutdown
  interface Serial2/0
   ip address 10.0.14.1 255.255.255.252
   no shutdown
  ```
- **Router 2 (Router 5)**:
  ```ios
  interface FastEthernet0/0
   ip address 10.0.0.1 255.255.248.0
   no shutdown
  interface Serial2/0
   ip address 10.0.14.2 255.255.255.252
   no shutdown
  ```
- **Static Route Configurations**:
  - **Router 1**: `ip route 10.0.0.0 255.255.248.0 10.0.14.2`
  - **Router 2**: `ip route 10.0.8.0 255.255.252.0 10.0.14.1`

---

## 📈 Verification Tests
End-to-end reachability has been successfully tested using ICMP echo requests (ping commands) in the Cisco Packet Tracer command terminal:
- **Task 1 Test**: PC0 (`196.10.0.2`) successfully pings PC2 (`196.10.0.66`) crossing the serial connection interface, confirming correct FLSM routing tables.
- **Task 2 Test**: PC0 (`10.0.8.2`) successfully pings PC4 (`10.0.0.2`), confirming correct VLSM routing tables and zero packet drops.
