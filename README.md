![Static Badge](https://img.shields.io/badge/github-Ncache-purple?logo=github)
![Static Badge](https://img.shields.io/badge/Docker-containing-grey?labelColor=2496ED&logo=docker&logoColor=white)

![Static Badge](https://img.shields.io/badge/Python-3.12-purple?labelColor=808080&logo=python&logoColor=white)
![Static Badge](https://img.shields.io/badge/Networking-purple?style=flat)

# Ncache

Ncache is a lightweight Python-based network scanner for host discovery and network analysis. It includes ARP scanning, ICMP scanning, passive discovery, host scanning, MAC vendor lookup, and local system information collection.

## Features
- ICMP scan for active host discovery
- ARP-based network scan
- Host scan for target IP analysis
- Passive network discovery
- MAC vendor lookup
- Local system information reporting
- Adjustable scan timing options

## Installation

- git clone https://github.com/Mata4r/Ncache.git
- cd Ncache
- pip install -r requirements.txt

## Usage
Run the scanner from the project root:

```bash
python ncache.py -As 192.168.1.0/24
```
```bash
python ncache.py -Is 192.168.1.0/24
```
```bash
python ncache.py -Ps 192.168.1.0
```
```bash
python ncache.py -Hs 192.168.1.0
```
```bash
python ncache.py -V 00:1A:2B:3C:4D:5E
```
```bash
python ncache.py -info
```

### Windows setup notes

- `scapy` on Windows requires an Npcap-compatible packet driver (Npcap). Install Npcap from https://nmap.org/npcap/ and enable "Support raw 802.11 traffic" only if you need wireless capture.
- Run scans from an elevated (Administrator) PowerShell/Command Prompt so raw packet operations work correctly.
- After installing Npcap, install Python dependencies:

```bash
pip install -r requirements.txt
```


## Notes
- This project is intended for authorized network analysis and learning purposes.
- Some features may require appropriate permissions depending on your environment.
