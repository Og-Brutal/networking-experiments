# Network Traffic Analysis with Wireshark

**Course:** CL3001 - Computer Networks  
**Lab:** 04 | Week 4  
**Campus:** National University of Computer & Emerging Sciences, Chiniot-Faisalabad  
**Instructor:** Esha Iftikhar  
**Student ID:** 23F3043

---

## Overview

This lab introduces hands-on network traffic analysis using **Wireshark**, an industry-standard open-source packet analyzer. The objective is to capture live HTTP traffic, dissect packet structures across multiple OSI layers, and interpret protocol-level data including IP headers, TCP headers, HTTP request/response fields, status codes, cookies, and redirect behavior.

By working directly with captured frames, this lab bridges the gap between theoretical networking concepts and real-world protocol behavior observable on any active network.

---

## Tool Used

**Wireshark** is a free and open-source network protocol analyzer. It captures data packets traveling through a network interface in real time and presents them in a structured, human-readable format. It is widely used in:

- Network troubleshooting and diagnostics
- Protocol research and education
- Cybersecurity monitoring and forensics
- Performance analysis

---

## Lab Structure

The lab is divided into four parts, each targeting a specific aspect of HTTP communication.

---

### Part A — Frame-Level Analysis (www.google.com.pk)

A live HTTP GET request was captured while navigating to `www.google.com.pk`. The very first frame in the capture was examined at the frame, IP, and TCP layers.

| Field | Value |
|---|---|
| Frame Direction | Outgoing |
| Source IP Address | 10.10.1.23 |
| Destination IP Address | 192.168.100.227 |
| Total Frame Size | 248 bytes |
| IP Header Size | 20 bytes |
| TCP Header Size | 20 bytes |
| Application Layer Payload | 34 bytes |

**Key Insight:** The standard IPv4 and TCP headers each consume exactly 20 bytes when no optional fields are present. The remaining bytes constitute the actual HTTP application data.

---

### Part B — HTTP Request Header Analysis (neverssl.com)

`http://neverssl.com` was opened to capture unencrypted plain-text HTTP traffic (this site intentionally never upgrades to HTTPS, making it ideal for educational packet inspection). The outgoing HTTP GET request was located and its headers were examined.

| HTTP Header Field | Captured Value |
|---|---|
| Accept-Language | en-US, en; q=0.9 |
| User-Agent | Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 |
| Connection | keep-alive |
| Host | coololdwonderousyawn.neverssl.com |

**Key Insight:** The `Connection: keep-alive` header instructs the server to maintain the TCP connection open for subsequent requests, reducing latency from repeated handshakes.

---

### Part C — HTTP Response Analysis

The HTTP response returned by the neverssl.com server was captured and analyzed.

| Response Field | Value |
|---|---|
| Status Code | 200 |
| Response Phrase | OK |
| Requested Host | http://neverssl.com |
| Accessed Host | coololdwonderousyawn.neverssl.com |
| Cookie Sent by Server | No |
| Content-Type | text/html |

**Key Insight:** The absence of a `Set-Cookie` header confirms the server is stateless for this session. The content type `text/html` confirms an HTML document was delivered.

---

### Part D — Extended Request/Response and 301 Redirect Behavior

A second navigation to `http://neverssl.com` was performed. This time, the full request-response cycle including a 301 redirect was traced.

#### Initial HTTP GET Request

| Field | Value |
|---|---|
| Browser Version | Chrome/145.0.0.0 |
| Connection Type | keep-alive |
| HTTP Method | GET |
| Time from GET to 200 OK | Measurable via Wireshark Time column (View > Time Display Format > Time of Day) |

#### Initial HTTP Response

| Field | Value |
|---|---|
| Status Code | 200 OK |
| Cookie Sent | No |
| Server Response Time | Visible in the HTTP Date response header (convert GMT to PST by adding 5 hours) |

#### Follow-up Request After 301 Redirect

When a server returns a `301 Moved Permanently` status, the browser automatically issues a new HTTP request to the redirect target without any user action.

| Field | Value |
|---|---|
| HTTP Method | GET |
| Connection Type | keep-alive |
| Host Header Value | neverssl.com |
| Host Difference Observed | User typed `neverssl.com`; the browser was redirected to the subdomain `coololdwonderousyawn.neverssl.com` |

#### Final HTTP Response (Post-Redirect)

| Field | Value |
|---|---|
| Status Code | 200 OK |
| Server Software | Apache |
| Content-Type | text/html |

**Key Insight:** The 301 redirect flow demonstrates how HTTP-level redirection works transparently. The browser follows the `Location` header from the 301 response and re-issues the GET request to the new address — all within milliseconds and invisible to the user.

---

## Concepts Demonstrated

```
OSI Layers Observed
-------------------
Layer 7  Application    HTTP GET / HTTP Response / Status Codes / Headers
Layer 4  Transport      TCP Header (20 bytes) / keep-alive connections
Layer 3  Network        IPv4 Header (20 bytes) / Source & Destination IPs
Layer 2  Data Link      Ethernet Frame / Total frame byte count
```

| Concept | What Was Learned |
|---|---|
| Packet Encapsulation | Each layer wraps the payload from the layer above it |
| HTTP Methods | GET is used to retrieve resources from a web server |
| Status Codes | 200 = Success, 301 = Permanent Redirect |
| Persistent Connections | keep-alive reduces TCP handshake overhead |
| User-Agent String | Browsers identify themselves through the User-Agent header |
| Cookie Behavior | Servers optionally set cookies via Set-Cookie response header |
| Redirect Chain | 301 responses trigger automatic browser re-requests |
| PST Conversion | GMT + 5 hours = Pakistan Standard Time |

---

## Screenshots

All Wireshark captures are included in the lab solution document and the generated PDF report. Screenshots cover:

- Frame capture for `www.google.com.pk` (Part A)
- HTTP request headers for `neverssl.com` (Part B)
- HTTP response fields (Part C)
- Full GET + redirect + final response cycle (Part D)

---

## Repository Structure

```
CN-Lab-04-Wireshark/
|
+-- README.md                      <- This file
+-- CN_LAB_04_Solution.pdf         <- Full professional lab report with analysis
+-- 23F3043_CN_LAB_04.docx         <- Original solution document with screenshots
+-- Lab_4_week_4.docx              <- Lab manual provided by instructor
```

---

## How to Reproduce This Lab

1. Download and install [Wireshark](https://www.wireshark.org/download.html)
2. Start a new capture on your active network interface
3. Open a browser and navigate to `http://neverssl.com`
4. In Wireshark, filter traffic using: `http`
5. Locate the HTTP GET request and inspect frame, IP, TCP, and HTTP layers
6. Locate the corresponding HTTP response and inspect status, headers, and body metadata
7. Use `View > Time Display Format > Time of Day` for readable timestamps

---

## References

- Wireshark Official Documentation: https://www.wireshark.org/docs/
- HTTP/1.1 Specification (RFC 7230): https://datatracker.ietf.org/doc/html/rfc7230
- HTTP Status Codes (RFC 7231): https://datatracker.ietf.org/doc/html/rfc7231
- IPv4 Header Format (RFC 791): https://datatracker.ietf.org/doc/html/rfc791
- TCP Specification (RFC 793): https://datatracker.ietf.org/doc/html/rfc793

---

## License

This repository is submitted as academic coursework for CL3001 - Computer Networks at NUCES Chiniot-Faisalabad. All content is for educational purposes.
