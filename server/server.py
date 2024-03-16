import socket
import threading

HEADER = 64
PORT = 9999
server = socket.gethostbyname(socket.gethostname())
ADDR= (server, PORT)
FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msg_length = conn.recv(64).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == "quit":
                connected = False
            print(f"[{addr}] {msg}")
            conn.send("Message received".encode('utf-8'))
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {server}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] Server is starting...")
start()


#server.listen(5)

#while True:
#    communication_socket, address = server.accept()
#   print(f"Connected to {address}")
#    message = communication_socket.recv(1024).decode('utf-8')
#    print(f"Message from Client is: {message}")
#    communication_socket.send(f"Got your Message! Thank you".encode('utf-8'))
#    communication_socket.close()
#    print(f"Connection with {address} ended!")
