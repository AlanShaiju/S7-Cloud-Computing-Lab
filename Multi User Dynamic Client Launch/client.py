import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(f"Reversed Message: {message}")
        except:
            print("Disconnected from server.")
            client_socket.close()
            break

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 5555))
    
    threading.Thread(target=receive_messages, args=(client_socket,)).start()

    while True:
        message = input("You: ")
        if message.lower() == "exit":
            client_socket.send(message.encode())
            client_socket.close()
            break
        client_socket.send(message.encode())

if __name__ == "__main__":
    start_client()
