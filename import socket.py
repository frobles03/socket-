import socket

def servidor():
    host = "127.0.0.1"
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((host, port))

    server_socket.listen(1)
    print(f"Esperando una conexión en {host}:{port}...")

    client_socket, client_address = server_socket.accept()
    print(f"Cliente conectado desde {client_address}")

    data = client_socket.recv(1024)
    print(f"Mensaje del cliente: {data.decode('utf-8')}")

    client_socket.close()
    server_socket.close()

def cliente():
    host = "127.0.0.1"
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    mensaje = "Hola, servidor!"
    client_socket.send(mensaje.encode('utf-8'))

    client_socket.close()

if __name__ == "__main__":
    import threading

    servidor_thread = threading.Thread(target=servidor)
    cliente_thread = threading.Thread(target=cliente)

    servidor_thread.start()
    cliente_thread.start()

    servidor_thread.join()
    cliente_thread.join()
