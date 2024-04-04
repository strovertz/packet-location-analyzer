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

#def count_ports(lista, lista2):
#    for i in lista:
#        x = i
#        d = Counter(lista2)
#        print('{} has occurred {} times'.format(x, d[x]))
#    print(lista)
#    print(lista2)

#@thread6.threaded()
def capture_package():
    lista = []; lista2 = []; ips = []; bit = 0
    prefix = ['172', '192', '10.',  '127', '255']
    with pydivert.WinDivert() as w:
        for packet in w:
            #if packet.dst_addr == "3.95.214.97": # ip instancia ec2 com um api/rest rodando em docker
            if packet.direction and packet.src_addr not in ips and packet.src_addr[:3] not in prefix: ips.append(packet.src_addr)
            print(packet)
            # para checar a porta, implementar if para validar direção e checagem jogar a porta em uma lista
            w.send(packet)
            if bit == 100: break
            bit+=1
            #else: continue
    return ips

def insert_locs(ips):
    address = process_ips(ips)
    mapa = create_map([-29.6894956, -53.811126])
    print(address)
    j = 0
    for i in address:
        print(f'IP DE I AQUI: {i}')
        infos = get_infos(ips[j])
        if len(i) > 1: mapa = set_markup(mapa, i, ips[j], infos)
        j+=1
    mapa = set_markup(mapa,[len(address)-2,len(address)-1], ips[len(ips)-1], get_infos(ips[len(ips)-1]))
    mapa.save("../map/my_map1.html")

    print('Mapa Salvo')

def main():
    #thread6.run_threaded(package_load)
    #thread6.run_threaded(capture_package)
    ips = capture_package()
    insert_locs(ips)

if __name__ == "__main__":
    main()
