import socket
import threading

# Client configurations
HOST = '127.0.0.1'  # Server IP
PORT = 5555  # Server port

nickname = input("Choose your nickname: ")

# Initialize client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Receive messages from the server
def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("An error occurred!")
            client.close()
            break

# Send messages to the server
def send_messages():
    while True:
        message = f"{nickname}: {input('')}"
        client.send(message.encode('utf-8'))
        if message.split(": ")[1] == "exit":
            client.send("exit".encode('utf-8'))
            client.close()
            break

# Start threads for receiving and sending messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.start()
