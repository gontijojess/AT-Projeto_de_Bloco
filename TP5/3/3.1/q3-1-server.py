import socket
import ssl

def servidor_eco_tls():
    host = '127.0.0.1'
    port = 10023
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((host, port))
        sock.listen(1)
        print(f"Servidor TLS ouvindo em {host}:{port} (Aguardando conexão)...")
        
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")
        
        with context.wrap_socket(sock, server_side=True) as ssock:
            conn, addr = ssock.accept()
            with conn:
                print(f"Conexão estabelecida com {addr}")
                
                dados = conn.recv(1024)
                mensagem = dados.decode('utf-8')
                print(f"Recebido: {mensagem}")
                conn.sendall(dados)

servidor_eco_tls()