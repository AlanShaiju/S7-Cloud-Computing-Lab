import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

class ServerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Server")

        # Create GUI components
        self.text_area = scrolledtext.ScrolledText(root, state='disabled')
        self.text_area.pack(expand=True, fill='both')

        self.entry = tk.Entry(root)
        self.entry.pack(fill='x')
        self.entry.bind('<Return>', self.send_message)

        # Set up the server
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('localhost', 12345))
        self.server_socket.listen(5)
        
        self.clients = {}  # Dictionary to hold client sockets and their usernames
        self.client_id = 0
        self.lock = threading.Lock()

        self.accept_thread = threading.Thread(target=self.accept_clients)
        self.accept_thread.start()
    
    def accept_clients(self):
        while True:
            client_socket, address = self.server_socket.accept()
            self.client_id += 1
            client_socket.send(f"ID:{self.client_id}".encode('utf-8'))
            
            with self.lock:
                self.clients[client_socket] = {"username": None}
            
            self.text_area.config(state='normal')
            self.text_area.insert('end', f"Client {address} connected with ID {self.client_id}.\n")
            self.text_area.config(state='disabled')
            
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        username = client_socket.recv(1024).decode('utf-8')
        with self.lock:
            self.clients[client_socket]["username"] = username

        self.broadcast_message(f"{username} has joined the chat.")
        
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                if message:
                    self.broadcast_message(f"{username}: {message}", client_socket)
            except:
                with self.lock:
                    self.clients.pop(client_socket, None)
                client_socket.close()
                break

    def broadcast_message(self, message, sender_socket=None):
        with self.lock:
            for client_socket in self.clients:
                if client_socket != sender_socket:
                    try:
                        client_socket.send(message.encode('utf-8'))
                    except:
                        client_socket.close()
                        self.clients.pop(client_socket, None)
        
        self.text_area.config(state='normal')
        self.text_area.insert('end', f"Broadcast: {message}\n")
        self.text_area.config(state='disabled')

    def send_message(self, event):
        message = self.entry.get()
        if message:
            self.broadcast_message(f"Server: {message}")
            self.entry.delete(0, 'end')

if __name__ == "__main__":
    root = tk.Tk()
    app = ServerApp(root)
    root.mainloop()
