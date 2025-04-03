from scapy.all import *
import sys
from collections import defaultdict

arp_table = defaultdict(str)

def get_mac_address(ip_address):
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request = ARP(pdst=ip_address)
    arp_request_broadcast = broadcast / arp_request
    answered_list = srp(arp_request_broadcast, timeout=1, verbose=False)
    return answered_list[0][0][1].hwsrc if answered_list else None

def detect_spoofing(packet):
    if packet.haslayer(ARP) and packet[ARP].op == 2:
        ip = packet[ARP].psrc
        mac = packet[ARP].hwsrc
        
        if packet[ARP].op == 2:
            print(f"[*] ARP Reply recebido: {ip} está em {mac}")
            
            if ip in arp_table and arp_table[ip] != mac:
                print(f"\n[!] ALERTA: Possível ARP Spoofing detectado para IP {ip}!")
                print(f"    MAC anterior: {arp_table[ip]}")
                print(f"    MAC atual:    {mac}\n")
        
        arp_table[ip] = mac

print("\nDetector de ARP Spoofing")
print("Monitorando a rede... Pressione Ctrl+C para parar\n")

try:
    sniff(filter="arp", prn=detect_spoofing, store=0)
    
except:
    print("\nOcorreu um erro...")
    sys.exit(0)

        