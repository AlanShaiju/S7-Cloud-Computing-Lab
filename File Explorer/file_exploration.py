import tkinter as tk
from tkinter import filedialog, messagebox

# Function to open a file and read its content
def open_file():
    # Ask the user to select a file
    file_path = filedialog.askopenfilename(title="Select a File")
    
    if file_path:  # Check if the user selected a file
        try:
            # Open the file in read mode with UTF-8 encoding and handle any character encoding errors
            with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
                content = file.read()
                text_area.delete(1.0, tk.END)  # Clear previous content in the text area
                text_area.insert(tk.END, content)  # Display file content in the text area
                replace_button.config(state=tk.NORMAL)  # Enable the replace button
                return file_path  # Return the selected file path
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while reading the file: {e}")
    return None

# Function to replace the given phrase in the content and save the modified content to the file
def replace_content():
    file_path = open_file()  # Get the selected file
    if file_path:
        old_phrase = old_phrase_entry.get()  # Get the old phrase to replace
        new_phrase = new_phrase_entry.get()  # Get the new phrase
        
        if old_phrase == "" or new_phrase == "":
            messagebox.showwarning("Input Error", "Please enter both old and new phrases.")
            return
        
        try:
            # Open the file in read mode to get the content
            with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
                content = file.read()
            
            # Replace the old phrase with the new phrase
            modified_content = content.replace(old_phrase, new_phrase)

            # Open the file in write mode to save the modified content
            with open(file_path, 'w', encoding='utf-8', errors='replace') as file:
                file.write(modified_content)
            
            # Inform the user that the operation was successful
            messagebox.showinfo("Success", f"The phrase '{old_phrase}' has been replaced with '{new_phrase}' in the file.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while modifying the file: {e}")

# Create the main window
root = tk.Tk()
root.title("File Phrase Replacer")

# Create and place widgets
open_button = tk.Button(root, text="Open File", command=open_file)
open_button.pack(pady=10)

text_area = tk.Text(root, height=15, width=50)
text_area.pack(pady=10)

old_phrase_label = tk.Label(root, text="Enter the phrase to replace:")
old_phrase_label.pack()

old_phrase_entry = tk.Entry(root, width=50)
old_phrase_entry.pack(pady=5)

new_phrase_label = tk.Label(root, text="Enter the new phrase:")
new_phrase_label.pack()

new_phrase_entry = tk.Entry(root, width=50)
new_phrase_entry.pack(pady=5)

replace_button = tk.Button(root, text="Replace Phrase", command=replace_content, state=tk.DISABLED)
replace_button.pack(pady=20)

# Run the application
root.mainloop()
