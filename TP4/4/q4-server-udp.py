import socket

host = '127.0.0.1'
port = 22222

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((host, port))

print(f"Servidor UDP escutando em {host}:{port}...")

while True: 
    message, address = server.recvfrom(1024)
    message = message.strip().decode("utf-8") 
    print(f"Mensagem recebida de {address}: {message}")

    server.sendto(b'ack', address)
    print(f"Resposta 'ack' enviada para {address}")
    
server.close()