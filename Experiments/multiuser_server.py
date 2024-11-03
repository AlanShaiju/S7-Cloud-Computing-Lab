import socket
import threading

# Server configurations
HOST = '127.0.0.1'  # Localhost
PORT = 5555  # Port to listen on

# Initialize server and list of connected clients
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
clients = []
nicknames = []

# Broadcast message to all connected clients
def broadcast(message):
    for client in clients:
        client.send(message)

# Handle incoming messages from a client
def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            if message.decode('utf-8') == 'exit':
                index = clients.index(client)
                nickname = nicknames[index]
                broadcast(f"{nickname} has left the chat.".encode('utf-8'))
                clients.remove(client)
                nicknames.remove(nickname)
                client.close()
                break
            else:
                broadcast(message)
        except:
            index = clients.index(client)
            nickname = nicknames[index]
            clients.remove(client)
            nicknames.remove(nickname)
            client.close()
            break

# Main function to receive clients
def receive_connections():
    while True:
        client, address = server.accept()
        print(f"Connected with {address}")

        client.send("NICK".encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} has joined the chat!".encode('utf-8'))
        client.send("Connected to the server!".encode('utf-8'))

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

print("Server is running...")
receive_connections()
