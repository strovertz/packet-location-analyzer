import pydivert
import requests
import thread6
from collections import Counter
from get_loc import *
from map import *

@thread6.threaded()
def package_load():
    for i in range(100):
        res = requests.get('http://ec2-3-95-214-97.compute-1.amazonaws.com:8080/health')
        print(res.text)
    exit()

def count_ports(lista, lista2):
    for i in lista:
        x = i
        d = Counter(lista2)
        print('{} has occurred {} times'.format(x, d[x]))
    print(lista)
    print(lista2)

#@thread6.threaded()
def capture_package():
    lista = []
    lista2 = []
    ips = []
    bit = 0
    with pydivert.WinDivert() as w:
        for packet in w:
            #if packet.dst_addr == "3.95.214.97": # ip instancia ec2 com um api/rest rodando em docker
            if packet.direction and packet.src_addr not in ips:
                ips.append(packet.src_addr)
            if not packet.direction:
                if packet.dst_port not in lista:
                    lista.append(packet.dst_port)
                lista2.append(packet.dst_port)
                print(packet)
                print('\n \n \n')
                bit+=1
            w.send(packet)
            if bit == 20:
                break
    count_ports(lista, lista2)
    return ips
            #else:
            #w.send(packet)

def insert_locs(ips):
    address = process_ips(ips)
    my_location = [-29.6894956, -53.811126]
    mapa = create_map(my_location)
    print(address)
    j = 0
    for i in address:
        if len(i) > 1: mapa = set_markup(mapa, i, ips[j])
        j+=1
    mapa = set_markup(mapa,[len(address)-2,len(address)-1], ips[len(ips)-1])
    mapa.save("map/my_map1.html")
    print('Mapa Salvo')

def main():
    #thread6.run_threaded(package_load)
    #thread6.run_threaded(capture_package)
    ips = capture_package()
    insert_locs(ips)

if __name__ == "__main__":
    main()
