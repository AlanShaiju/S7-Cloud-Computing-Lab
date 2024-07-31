import socket

def start_client(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        print(f"Connected to server at {host}:{port}")

        while True:
            message = input("Enter message to send (type 'exit' to quit): ")
            if message.lower() == 'exit':
                client_socket.sendto(message.encode(), (host, port))
                print("Closing connection.")
                break
            client_socket.sendto(message.encode(), (host, port))
            data, server = client_socket.recvfrom(1024)
            print(f"Received from server: {data.decode()}")

if __name__ == "__main__":
    start_client()
