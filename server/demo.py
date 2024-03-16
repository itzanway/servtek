import socket
import threading

PORT = 9999

server = socket.gethostbyname(socket.gethostname())
print(f"Server IP: {server}")

print(socket.gethostname())