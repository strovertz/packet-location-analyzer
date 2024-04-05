import pydivert
import requests
import thread6
from scapy.utils import RawPcapReader
from scapy.layers.l2 import Ether
from scapy.layers.inet import IP
from collections import Counter
from get_loc import *
from map import *

@thread6.threaded()
def package_load():
    for i in range(100):
        res = requests.get('http://ec2-3-95-214-97.compute-1.amazonaws.com:8080/health')
        print(res.text)
    exit()

#def count_ports(lista, lista2):
#    for i in lista:
#        x = i
#        d = Counter(lista2)
#        print('{} has occurred {} times'.format(x, d[x]))
#    print(lista)
#    print(lista2)

#@thread6.threaded()
# Use para ler os pacotes que da rede
def capture_package():
    lista = []; lista2 = []; ips = []; bit = 0
    prefix = ['172', '192', '10.', '127', '255', 'fe8']
    with pydivert.WinDivert() as w:
        for packet in w:
            #if packet.dst_addr == "3.95.214.97": # ip instancia ec2 com um api/rest rodando em docker
            if packet.direction and packet.src_addr not in ips and packet.src_addr[:3] not in prefix: ips.append(packet.src_addr)
            print(packet)
            # para checar a porta, implementar if para validar direção e checagem jogar a porta em uma lista
            w.send(packet)
            if bit == 300: break
            bit+=1
            #else: continue
    return ips

# use pra ler pacotes de um arquivo pcap
def read_pcap(file_path):
    pcap_ips = []
    prefix = ['172', '192', '10.', '127', '255', 'fe8']
    for (packet_data, packet_metadata,) in RawPcapReader(file_path):
        packet_eth = Ether(packet_data)
        #ignora se nao for ipv4
        if packet_eth.type != 0x0800:
            continue
        packet_ip = packet_eth[IP]
        if packet_ip.proto != 6:
           continue
        if packet_ip.src[:3] not in prefix and packet_ip.src not in pcap_ips: pcap_ips.append(packet_ip.src)
    return pcap_ips



def insert_locs(ips):
    address = process_ips(ips)
    mapa = create_map([-29.6894956, -53.811126])
    print(address)
    j = 0
    for i in address:
        if len(i) > 1: infos = get_infos(ips[j]); mapa = set_markup(mapa, i, ips[j], infos); print(f'Lat,Lon de ip \'{j}\': {i}')
        j+=1
    if len(address) > 0: mapa = set_markup(mapa,[len(address)-2,len(address)-1], ips[len(ips)-1], get_infos(ips[len(ips)-1]))
    mapa.save("../map/my_map1.html")

    print('Mapa Salvo')

def main():
    file_path = "files/trabalho1.pcapng"
    #thread6.run_threaded(package_load)
    #thread6.run_threaded(capture_package)
    #ips = capture_package()
    ips2 = read_pcap(file_path)
    insert_locs(ips2)

if __name__ == "__main__":
    main()
