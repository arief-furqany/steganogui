import tkinter as tk
from tkinter import messagebox
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import base64

# Encryption Function
def encrypt(plain_text, key):
    try:
        des = DES.new(key, DES.MODE_ECB)
        padded_text = pad(plain_text.encode('utf-8'), DES.block_size)
        encrypted_text = des.encrypt(padded_text)
        return base64.b64encode(encrypted_text).decode('utf-8')
    except Exception as e:
        messagebox.showerror("Error", f"Encryption Error: {e}")
        return ""

# Decryption Function
def decrypt(encrypted_text, key):
    try:
        des = DES.new(key, DES.MODE_ECB)
        decoded_encrypted_text = base64.b64decode(encrypted_text)
        decrypted_text = unpad(des.decrypt(decoded_encrypted_text), DES.block_size)
        return decrypted_text.decode('utf-8')
    except Exception as e:
        messagebox.showerror("Error", f"Decryption Error: {e}")
        return ""

# GUI Functionality
def perform_encryption():
    plain_text = plain_text_entry.get()
    key = key_entry.get()

    if len(key) != 8:
        messagebox.showerror("Error", "Key must be exactly 8 characters long!")
        return

    encrypted_text = encrypt(plain_text, key.encode('utf-8'))
    encrypted_text_var.set(encrypted_text)

def perform_decryption():
    encrypted_text = encrypted_text_entry.get()
    key = key_entry.get()

    if len(key) != 8:
        messagebox.showerror("Error", "Key must be exactly 8 characters long!")
        return

    decrypted_text = decrypt(encrypted_text, key.encode('utf-8'))
    decrypted_text_var.set(decrypted_text)

# Initialize GUI Window
window = tk.Tk()
window.title("DES Encryption/Decryption")
window.geometry("400x400")

# Plain Text Input
tk.Label(window, text="Plain Text:").pack(pady=5)
plain_text_entry = tk.Entry(window, width=40)
plain_text_entry.pack(pady=5)

# Key Input
tk.Label(window, text="Key (8 characters):").pack(pady=5)
key_entry = tk.Entry(window, width=40, show="*")
key_entry.pack(pady=5)

# Encrypt Button
encrypt_button = tk.Button(window, text="Encrypt", command=perform_encryption)
encrypt_button.pack(pady=10)

# Encrypted Text Output
tk.Label(window, text="Encrypted Text:").pack(pady=5)
encrypted_text_var = tk.StringVar()
encrypted_text_entry = tk.Entry(window, textvariable=encrypted_text_var, width=40, state="readonly")
encrypted_text_entry.pack(pady=5)

# Decrypt Button
decrypt_button = tk.Button(window, text="Decrypt", command=perform_decryption)
decrypt_button.pack(pady=10)

# Decrypted Text Output
tk.Label(window, text="Decrypted Text:").pack(pady=5)
decrypted_text_var = tk.StringVar()
decrypted_text_entry = tk.Entry(window, textvariable=decrypted_text_var, width=40, state="readonly")
decrypted_text_entry.pack(pady=5)

# Run the GUI Event Loop
window.mainloop()

