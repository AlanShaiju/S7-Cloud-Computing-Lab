import socket

def start_server(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((host, port))
        print(f"Server listening on {host}:{port}")

        while True:
            data, addr = server_socket.recvfrom(1024)
            message = data.decode()
            print(f"Received message from {addr}: {message}")
            
            if message.lower() == 'exit':
                print(f"Received exit command from {addr}. Closing connection.")
                break

            response = input("Enter response: ")
            server_socket.sendto(response.encode(), addr)

    print("Server has shut down.")

if __name__ == "__main__":
    start_server()
