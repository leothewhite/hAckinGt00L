import socket

client_sockets = []

HOST = '210.121.159.217'
PORT = 15432

print('>> Server Start with ip :', HOST)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))

server_socket.listen()

try:
    print(">> Waiting...")
    client_socket, addr = server_socket.accept()

    while True:
        # 클라이언트로부터 요청 받기
        data = client_socket.recv(1024).decode("utf-8")
        if not data:
            continue

        # 요청 파싱
        parts = data.split("&&")
        if len(parts) != 0:
            print(parts[0])
        else:
            response = "유효하지 않은 요청"

except Exception as e:
    print("EXCEPTION 에러: ", e)