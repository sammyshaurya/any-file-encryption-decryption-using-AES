from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import filedialog
import os

# select file
def select_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

def decrypt(key, data):
    cipher = Fernet(key)
    decrypted = cipher.decrypt(data)
    return decrypted

selected_file = select_file()
filename, _ = os.path.splitext(os.path.basename(selected_file))

with open(filename + '.key', 'rb') as file:
    key = file.read()
    
with open(selected_file, 'rb') as file:
    file_to_decrypt = file.read()

# Corrected output filename construction
with open(filename, 'wb') as file:
    file.write(decrypt(key, file_to_decrypt))