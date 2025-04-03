from scapy.all import *
import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

def arp_scan(network):
    print(f"\n[*] Iniciando varredura ARP na rede {network}")
    
    arp_request = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=network)
    answered, _ = srp(arp_request, timeout=2, verbose=False)
    
    hosts = []
    for sent, received in answered:
        hosts.append((received.psrc, received.hwsrc))
    
    return hosts
    
network = '192.168.15.1/24'

try:
    hosts = arp_scan(network)
    
    if not hosts:
        print("Nenhum host encontrado")
    else:
        print("\nHosts ativos na rede:")
        for ip, mac in hosts:
            print(f"IP: {ip}, MAC: {mac}")
        
        print(f"\nTotal de hosts encontrados: {len(hosts)}")

except:
    print("Ocorreu um erro")