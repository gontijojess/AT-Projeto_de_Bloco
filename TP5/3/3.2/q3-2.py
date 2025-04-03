import socket
import ssl

def cliente_tls():
    host = '127.0.0.1'
    port = 10023
    message = "Mensagem segura com logging de pacotes"

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    try:
        ssock = context.wrap_socket(sock, server_hostname=host)

        original_send = ssock.send
        def logged_send(data, *args, **kwargs):
            print(f"Interceptado (envio): {data.tobytes()}")
            return original_send(data, *args, **kwargs)
        ssock.send = logged_send

        original_recv = ssock.recv
        def logged_recv(*args, **kwargs):
            data = original_recv(*args, **kwargs)
            if data:
                print(f"Interceptado (recebido): {data}")
            return data
        ssock.recv = logged_recv

        ssock.connect((host, port))
        print("Cliente: conexão estabelecida")

        ssock.sendall(message.encode('utf-8'))

        dados = ssock.recv(1024)
        print(f"Cliente: recebido: {dados.decode('utf-8')}")

    finally:
        ssock.close()

cliente_tls()