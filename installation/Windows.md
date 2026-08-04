# Windows installation

- Run CMD as administrator
- git clone https://github.com/Mata4r/Ncache.git
- cd Ncache
- pip install -r requirements.txt
- Run your first script e.g.
`python ncache.py -As [Subnet]`


## Windows setup notes

- `scapy` on Windows requires an Npcap-compatible packet driver (Npcap). Install Npcap from https://nmap.org/npcap/ and enable "Support raw 802.11 traffic" only if you need wireless capture.
- Run scans from an elevated (Administrator) PowerShell/Command Prompt so raw packet operations work correctly.
- After installing Npcap, install Python dependencies:

```bash
pip install -r requirements.txt
```
