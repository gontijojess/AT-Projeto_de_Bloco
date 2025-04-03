import socket

server_ip = 'localhost'
server_port = 22222

try:
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.connect((server_ip, server_port))

    message = socket.recv(1024)
    print(message.decode("utf-8"))
    while True:
        message = input("Digite sua mensagem: ")
        socket.send(bytes(message.encode('utf-8')))
        if message.lower() == "sair":
            break 
        message = socket.recv(1024)
        print(message.decode("utf-8"))
except socket.errno as error:
    print(f"Erro: {error}")
finally: socket.close()