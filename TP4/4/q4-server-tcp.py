import socket

server_ip = 'localhost'
server_port = 22222

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((server_ip, server_port))

server.listen(1)
print("Servidor aguardando conexão...")

conn, addr = server.accept()
mensagem_boas_vindas = "Conexão estabelecida. Seja bem-vindo ao Servidor!"

conn.send(mensagem_boas_vindas.encode("utf-8"))

while True:
    try:
        message = conn.recv(1024)
        print(message.decode("utf-8"))
        if message.lower() == "sair":
            break
        elif message:
            mensagem_recebida = "Sua mensagem foi recebida com sucesso!"
            conn.send(mensagem_recebida.encode("utf-8"))
        else:
            break
    except ConnectionResetError:
        print("Conexão fechada pelo cliente! Encerrando servidor...")
        break
    except Exception as e:
        print(f"Erro: {e}")
        break
conn.close()
server.close()