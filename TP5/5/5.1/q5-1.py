import time
import matplotlib.pyplot as plt
import dns.resolver

def dns_recon(domain):
    results = {}
    record_types = ['A', 'NS', 'MX']
    
    for record_type in record_types:
        try:
            print(f"Consultando registros {record_type} para {domain}")
            answers = dns.resolver.resolve(domain, record_type)
            results[record_type] = [str(answer) for answer in answers]
        except dns.resolver.NoAnswer:
            results[record_type] = []
        except Exception as e:
            print(f"Erro ao consultar registros {record_type} - {e}")
        
    return results

def calcular_tempo_dns_recon(domains, repetitions=3):
    times = []
    results = []
    
    for domain in domains:
        domain_times = []
        for _ in range(repetitions):
            start_time = time.time()
            result = dns_recon(domain)
            end_time = time.time()
            domain_times.append(end_time - start_time)
        
        avg_time = sum(domain_times) / len(domain_times)
        times.append(avg_time)
        results.append(result)
    
    return times, results

def plot_resultados(dns_times, domains):
    plt.figure(figsize=(15, 5))
    
    plt.subplot(1, 2, 1)
    plt.bar(range(len(domains)), dns_times, color='blue', alpha=0.6)
    plt.title('Tempo de exeução - DNS Recon')
    plt.xlabel('Domínio (índice)')
    plt.ylabel('Tempo de execução (segundos)')
    plt.grid(True)
  
    plt.subplot(1, 2, 2)
    plt.plot(range(len(domains)), dns_times, 'b-o')
    plt.yscale('log')
    plt.title('Tempo de exeução - DNS Recon (Escala Logarítmica)')
    plt.xlabel('Domínio (índice)')
    plt.ylabel('Tempo de execução (segundos)')
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

def print_estatisticas(dns_times):
    print("\nEstatísticas:")
    
    print("\nDNS Recon:")
    print(f"Minimum time: {min(dns_times):.3f} seconds")
    print(f"Maximum time: {max(dns_times):.3f} seconds")
    print(f"Average time: {sum(dns_times)/len(dns_times):.3f} seconds")

if __name__ == "__main__":
    dominios_teste = [
        "example.com",
        "google.com",
        "microsoft.com",
        "amazon.com",
        "github.com"
    ]
    
    
    print("\nTempo de execução DNS Recon:")
    dns_times, dns_results = calcular_tempo_dns_recon(dominios_teste)

    plot_resultados(dns_times, dominios_teste)
    
    print_estatisticas(dns_times)
    
    print("\nAmostra do resultado o microsoft.com:")
    print(dns_results[2])