import socket

client_sockets = []

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999

print('>> Server Start with ip :', HOST)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))

server_socket.listen()

try:
    while True:
        print(">> Waiting...")

        client_socket, addr = server_socket.accept()
        client_sockets.append(client_socket)
except Exception as e:
    print("Error:", e)
finally:
    server_socket.close()