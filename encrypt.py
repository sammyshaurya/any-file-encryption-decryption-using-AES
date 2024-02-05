from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import filedialog
import os

# create key
key = Fernet.generate_key()

# select file
def select_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

def encrypt_data(key, data):
    cipher = Fernet(key)
    encrypted_file = cipher.encrypt(data)
    return encrypted_file

selected_file = select_file()

with open(selected_file, 'rb') as file:
    data_to_encrypt = file.read()
    encrypted = encrypt_data(key, data_to_encrypt)

# Get the base name of the selected file
file_base_name = os.path.basename(selected_file)

encrypted_file_path = file_base_name + '.enc'
with open(encrypted_file_path, 'wb') as file:
    file.write(encrypted)

with open(file_base_name + '.key', 'wb') as file:
    file.write(key)

print(f"Encryption successful. Encrypted file: '{encrypted_file_path}', Key file: '{file_base_name}'.")