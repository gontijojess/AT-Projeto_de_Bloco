import dns.resolver

def dns_recon(domain):
    print(f"\nConsultas DNS para o domínio: {domain}\n")
    
    try:
        print("Registros A:")
        answers_a = dns.resolver.resolve(domain, 'A')
        for rdata in answers_a:
            print(f"    {rdata.address}")
    except:
        print("Erro ao consultar registros A")
    
    try:
        print("\nRegistros MX:")
        answers_mx = dns.resolver.resolve(domain, 'MX')
        for rdata in answers_mx:
            print(f"    {rdata.preference} {rdata.exchange}")
    except:
        print("Erro ao consultar registros MX")
    
    try:
        print("\nRegistros NS:")
        answers_ns = dns.resolver.resolve(domain, 'NS')
        for rdata in answers_ns:
            print(f"    {rdata.target}")
    except:
        print("Erro ao consultar registros NS")


dominio = 'example.com'
dns_recon(dominio)