import socket
import threading
import subprocess
import re

# Function to reverse message text while preserving punctuation
def reverse_message_with_punctuation(message):
    def reverse_word(word):
        letters = [c for c in word if c.isalpha()]
        reversed_word = ''.join(letters[::-1])
        result = []
        reverse_idx = 0
        for char in word:
            if char.isalpha():
                result.append(reversed_word[reverse_idx])
                reverse_idx += 1
            else:
                result.append(char)
        return ''.join(result)
    
    return ' '.join(reverse_word(word) for word in message.split())

# Broadcast message to all clients
def broadcast(message, clients, sender_socket):
    for client in clients:
        if client != sender_socket:
            client.send(message.encode())

# Handle individual client connection
def handle_client(client_socket, clients):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message.lower() == "exit":
                clients.remove(client_socket)
                client_socket.close()
                break
            reversed_message = reverse_message_with_punctuation(message)
            broadcast(reversed_message, clients, client_socket)
        except:
            clients.remove(client_socket)
            client_socket.close()
            break

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 5555))
    server.listen(5)
    print("Server is running and waiting for connections...")

    # Ask for the number of clients to launch
    num_clients = int(input("Enter the number of clients to launch: "))

    clients = []

    # Launch each client in a new terminal
    for _ in range(num_clients):
        subprocess.Popen(["python", "client.py"])

    # Handle incoming connections
    while True:
        client_socket, client_address = server.accept()
        print(f"Client connected from {client_address}")
        clients.append(client_socket)
        threading.Thread(target=handle_client, args=(client_socket, clients)).start()

if __name__ == "__main__":
    start_server()
