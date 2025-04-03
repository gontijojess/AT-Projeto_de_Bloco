import ipaddress

def validar_ip_em_prefixo(ip, prefixo):
    ip_obj = ipaddress.ip_address(ip)
    prefixo_obj = ipaddress.ip_network(prefixo)
    return ip_obj in prefixo_obj

ip = "192.168.1.5"
prefixo = "192.168.1.0/24"
resultado = validar_ip_em_prefixo(ip, prefixo)
print(f"O IP {ip} está dentro do prefixo {prefixo}: {resultado}")