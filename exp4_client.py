import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
from tkinter import simpledialog

class ClientApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Client")

        # Create GUI components
        self.text_area = scrolledtext.ScrolledText(root, state='disabled')
        self.text_area.pack(expand=True, fill='both')

        self.entry = tk.Entry(root)
        self.entry.pack(fill='x')
        self.entry.bind('<Return>', self.send_message)

        # Set up the client
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('localhost', 12345))
        
        self.client_id = self.client_socket.recv(1024).decode('utf-8')
        self.username = simpledialog.askstring("Username", "Enter your username:", parent=self.root)
        self.client_socket.send(self.username.encode('utf-8'))

        self.listen_thread = threading.Thread(target=self.listen_for_messages)
        self.listen_thread.start()

    def listen_for_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if message:
                    self.text_area.config(state='normal')
                    self.text_area.insert('end', f"{message}\n")
                    self.text_area.config(state='disabled')
            except:
                break

    def send_message(self, event):
        message = self.entry.get()
        if message:
            self.client_socket.send(message.encode('utf-8'))
            self.text_area.config(state='normal')
            self.text_area.insert('end', f"{self.username}: {message}\n")
            self.text_area.config(state='disabled')
            self.entry.delete(0, 'end')

if __name__ == "__main__":
    root = tk.Tk()
    app = ClientApp(root)
    root.mainloop()
