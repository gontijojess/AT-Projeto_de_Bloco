import socket

host = '127.0.0.1'
port = 22222

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input("Digite sua mensagem: ")
    client.sendto(bytes(message.encode('utf-8')), (host, port))
    print(f"Mensagem '{message}' enviada para o servidor {host}:{port}")
    if message.lower() == "sair":
        break 
    response, server_addr = client.recvfrom(1024)
    print(f"Resposta recebida do servidor: {response.decode("utf-8")}")

client.close()