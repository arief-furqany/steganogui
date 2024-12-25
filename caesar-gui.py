import tkinter as tk
from tkinter import ttk

# Encryption function
def encrypt(plain_text, shift):
    cipher_text = ""
    for char in plain_text:
        if char.isupper():
            cipher_text += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            cipher_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            cipher_text += char
    return cipher_text

# Decryption function
def decrypt(cipher_text, shift):
    plain_text = ""
    for char in cipher_text:
        if char.isupper():
            plain_text += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            plain_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            plain_text += char
    return plain_text

# Fungsi GUI handle
def handle_encrypt():
    plain_text = entry_plain.get()
    shift = int(entry_shift.get())
    encrypted_text = encrypt(plain_text, shift)
    entry_cipher.delete(0, tk.END)
    entry_cipher.insert(0, encrypted_text)

# Fungsi GUI handle
def handle_decrypt():
    cipher_text = entry_cipher.get()
    shift = int(entry_shift.get())
    decrypted_text = decrypt(cipher_text, shift)
    entry_decrypt.delete(0, tk.END)
    entry_decrypt.insert(0, decrypted_text)

# GUI setup
root = tk.Tk()
root.title("Caesar Cipher GUI")
root.geometry("400x300")
root.configure(bg="#2C2C2C")  # Gray background

# Styles
style = ttk.Style()
style.configure("TLabel", background="#2C2C2C", foreground="white", font=("Arial", 12))
style.configure("TEntry", font=("Arial", 12))
style.configure("TButton", font=("Arial", 10), background="#888888", relief="flat")
style.map("TButton", background=[("active", "#555555")])

# Plain Text
label_plain = ttk.Label(root, text="Plain Text:")
label_plain.pack(pady=5)
entry_plain = ttk.Entry(root, width=30, font=("Arial", 12))
entry_plain.pack(pady=5)

# Shift Key
label_shift = ttk.Label(root, text="Shift Key:")
label_shift.pack(pady=5)
entry_shift = ttk.Entry(root, width=10, font=("Arial", 12))
entry_shift.pack(pady=5)

# Encrypt Button
button_encrypt = ttk.Button(root, text="Encrypt", command=handle_encrypt)
button_encrypt.pack(pady=5)

# Cipher Text
label_cipher = ttk.Label(root, text="Cipher Text:")
label_cipher.pack(pady=5)
entry_cipher = ttk.Entry(root, width=30, font=("Arial", 12))
entry_cipher.pack(pady=5)

# Decrypt Button
button_decrypt = ttk.Button(root, text="Decrypt", command=handle_decrypt)
button_decrypt.pack(pady=5)

# Decrypted Text
label_decrypt = ttk.Label(root, text="Decrypted Text:")
label_decrypt.pack(pady=5)
entry_decrypt = ttk.Entry(root, width=30, font=("Arial", 12))
entry_decrypt.pack(pady=5)

# Run the main loop
root.mainloop()
