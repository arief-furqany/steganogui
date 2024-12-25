import os
from stegano import lsb
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import ttkbootstrap as tb

def get_image_path():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg")])
    if file_path:
        return file_path
    else:
        return None

def hide_message_gui():
    img_path = get_image_path()
    if not img_path:
        messagebox.showerror("Error", "Path gambar tidak valid atau tidak dipilih.")
        return

    message = message_entry.get()
    if not message:
        messagebox.showerror("Error", "Pesan tidak boleh kosong.")
        return

    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if not save_path:
        messagebox.showerror("Error", "Path untuk menyimpan gambar tidak valid atau tidak dipilih.")
        return

    try:
        secret = lsb.hide(img_path, message)
        secret.save(save_path)
        messagebox.showinfo("Success", f"Pesan berhasil disembunyikan dalam gambar.\nGambar disimpan di: {save_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Gagal menyimpan gambar: {e}")

def show_message_gui():
    img_path = get_image_path()
    if not img_path:
        messagebox.showerror("Error", "Path gambar tidak valid atau tidak dipilih.")
        return

    try:
        clear_message = lsb.reveal(img_path)
        if clear_message:
            hidden_message_textbox.config(state="normal")
            hidden_message_textbox.delete("1.0", tk.END)
            hidden_message_textbox.insert(tk.END, clear_message)
            hidden_message_textbox.config(state="disabled")
        else:
            messagebox.showinfo("Info", "Tidak ada pesan tersembunyi dalam gambar ini.")
    except Exception as e:
        messagebox.showerror("Error", f"Gagal menampilkan pesan dari gambar: {e}")

def exit_app():
    root.destroy()

# GUI Setup
root = tb.Window(themename="darkly")
root.title("Steganography Tool - GUI Version")
root.geometry("420x500")
root.configure(bg="#001f3f")  # Warna biru dongker

# Widgets
frame = ttk.Frame(root, padding=15)
frame.pack(expand=True)

title_label = ttk.Label(frame, text="Steganography Tool", font=("Helvetica", 18, "bold"), foreground="white")
title_label.pack(pady=15)

message_label = ttk.Label(frame, text="Pesan Rahasia:", foreground="white", font=("Helvetica", 12))
message_label.pack()

message_entry = ttk.Entry(frame, width=40)
message_entry.pack(pady=10)

hide_button = ttk.Button(
    frame, text="Sembunyikan Pesan", command=hide_message_gui, bootstyle="info-outline", width=30
)
hide_button.pack(pady=10)

reveal_button = ttk.Button(
    frame, text="Tampilkan Pesan", command=show_message_gui, bootstyle="info-outline", width=30
)
reveal_button.pack(pady=10)

hidden_message_label = ttk.Label(frame, text="Pesan Tersembunyi:", foreground="white", font=("Helvetica", 12))
hidden_message_label.pack(pady=10)

hidden_message_textbox = tk.Text(frame, height=5, width=40, bg="#001f3f", fg="white", wrap="word", relief="solid", borderwidth=1)
hidden_message_textbox.pack(pady=10)
hidden_message_textbox.config(state="disabled")

exit_button = ttk.Button(frame, text="Keluar", command=exit_app, bootstyle="danger-outline", width=30)
exit_button.pack(pady=20)

# Run the GUI
root.mainloop()

