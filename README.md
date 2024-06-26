# packet-location-analyzer


## About

The program captures network packets, filtering the destination IP (your network) and some source IPs (packet-location-analyzer/src/trabalho1.pcapng) through IP location and creates a markup on an html page generated using folium

## Usage

Clone this repo and navigate to 'src' folder
```bash
git clone https://github.com/strovertz/packet-location-analyzer.
```
```
cd packet-location-analyzer/src
```
Run the command bellow to capture packets and generate your map
```
python main.py
```

## Data Available
```json
'User IP': '20.0.28.08'
'CountryName': 'Brazil'
'UsageType': 'Data Center/Web Hosting/Transit'
'Isp': 'Example Corporation | Internet Service Provider'
'Domain': 'microsoft.com | IP Domain'
'isTor': 'False'
'abuseConfidenceScore': 0
```
#### abuseConfidenceScore |
 ```
 AbuseConfidenceScore is our calculated evaluation on how abusive the IP is based on the users that reported it
 ```
#### UsageType possible values:
```
- Commercial
- Organization
- Government
- Military
- University/College/School
- Library
- Content Delivery Network
- Fixed Line ISP
- Mobile ISP
- Data Center/Web Hosting/Transit
- Search Engine Spider
- Reserved
```

##### Folium Tile:
Earth At Night
```python
tiles="https://demo.ldproxy.net/earthatnight/tiles/WebMercatorQuad/{z}/{y}/{x}?f=jpeg", attr='EarthAtNight'
```


 <b>AbuseIPDB</b>: https://docs.abuseipdb.com/#check-endpoint

<b>Gleison</b>: github.com/strovertz
<b><br>Felipe Sanfelice</b>:
<b><br>Giovanni Roman</b>:
<b><br>Francisco Ribas</b>:
