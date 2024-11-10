import socket
import tkinter as tk
from tkinter import scrolledtext, messagebox

# Function to send words to the server and receive the response
def send_words():
    words = entry.get()
    if not words:
        messagebox.showwarning("Input Error", "Please enter a list of words.")
        return

    # Connect to the server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 5555))
    
    # Send words to the server
    client.send(words.encode())
    
    # Receive the response from the server
    response = client.recv(1024).decode()
    
    # Display the response in the text box
    result_text.config(state="normal")
    result_text.delete(1.0, tk.END)  # Clear previous results
    result_text.insert(tk.END, response)
    result_text.config(state="disabled")
    client.close()

# Setup client GUI
root = tk.Tk()
root.title("Palindrome Checker Client")
tk.Label(root, text="Enter a comma-separated list of words:").pack(pady=5)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)
send_button = tk.Button(root, text="Send to Server", command=send_words)
send_button.pack(pady=10)
result_text = scrolledtext.ScrolledText(root, width=50, height=10, state="disabled")
result_text.pack(pady=5)
root.mainloop()