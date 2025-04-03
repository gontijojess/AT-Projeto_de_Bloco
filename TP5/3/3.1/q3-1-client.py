# openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes -subj "/CN=localhost"

import socket
import ssl

def cliente_tls():
    host = '127.0.0.1'
    port = 10023
    message = "Olá, servidor TLS!"
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            ssock.connect((host, port))
            print("Cliente: conexão estabelecida")
            
            ssock.sendall(message.encode('utf-8'))
            
            dados = ssock.recv(1024)
            print(f"Cliente: recebido: {dados.decode('utf-8')}")

cliente_tls()