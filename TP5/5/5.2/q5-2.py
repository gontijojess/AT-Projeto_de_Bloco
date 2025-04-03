import subprocess

def run_nmap_scan(target):
    print(f"\n[+] Iniciando scan Nmap no alvo: {target}\n")
    
    try:
        command = ["nmap", "-sV", target]
        
        result = subprocess.run(command, 
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              text=True)
        
        if result.returncode != 0:
            print(f"[!] Erro ao executar Nmap: {result.stderr}")
            return
        
        print("=== RESULTADOS DO SCAN ===")
        print(result.stdout)
        
    except:
        print("Ocorreu um erro!")

target = "192.168.15.1"
run_nmap_scan(target)