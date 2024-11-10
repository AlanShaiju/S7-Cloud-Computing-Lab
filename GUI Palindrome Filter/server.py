import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

# Function to check if a word is a palindrome
def is_palindrome(word):
    return word == word[::-1]

# Handle each client connection
def handle_client(client_socket, addr):
    try:
        words_data = client_socket.recv(1024).decode()
        words_list = words_data.split(",")  # Assuming comma-separated words

        # Find palindromes
        palindromes = [word for word in words_list if is_palindrome(word)]
        num_palindromes = len(palindromes)

        # Prepare response
        response = f"Number of palindromes: {num_palindromes}\nPalindromes: {', '.join(palindromes)}"
        
        # Send the response back to the client
        client_socket.send(response.encode())

        # Update the GUI with the results
        server_text.config(state="normal")
        server_text.insert(tk.END, f"Client {addr} sent words: {words_list}\n")
        server_text.insert(tk.END, f"Palindromes found: {palindromes}\n\n")
        server_text.config(state="disabled")
    except Exception as e:
        print("Error handling client:", e)
    finally:
        client_socket.close()

# Start the server
def start_server():
    server_text.config(state="normal")
    server_text.insert(tk.END, "Server is starting...\n")
    server_text.config(state="disabled")

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 5555))
    server.listen(5)
    server_text.insert(tk.END, "Server is running and waiting for connections...\n")

    def accept_connections():
        while True:
            client_socket, addr = server.accept()
            threading.Thread(target=handle_client, args=(client_socket, addr)).start()
            server_text.config(state="normal")
            server_text.insert(tk.END, f"Client {addr} connected.\n")
            server_text.config(state="disabled")

    threading.Thread(target=accept_connections).start()

# Setup server GUI
root = tk.Tk()
root.title("Palindrome Checker Server")

start_button = tk.Button(root, text="Start Server", command=start_server)
start_button.pack(pady=5)

server_text = scrolledtext.ScrolledText(root, width=50, height=20, state="disabled")
server_text.pack(pady=10)

root.mainloop()
