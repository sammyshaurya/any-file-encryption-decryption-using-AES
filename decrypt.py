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
    try:
        cipher = Fernet(key)
        decrypted = cipher.decrypt(data)
        return decrypted
    except Exception as e:
        print(f"Error during decryption: {e}")
        exit()

selected_file = select_file()
while not selected_file:
    print("No file selected, trying again")
    selected_file = select_file()

filename, _ = os.path.splitext(os.path.basename(selected_file))
if os.path.exists(filename):
    print("Already encrypted file present")
    exit()
    
if selected_file[-4:] != '.enc':
    print("Selected file is not an encrypted file, (.enc), exiting")

try:
    with open(filename + '.key', 'rb') as file:
        key = file.read()
except:
    print("key not found, please locate the file and insert to the folder")
    exit()
    
with open(selected_file, 'rb') as file:
    file_to_decrypt = file.read()

with open(filename, 'wb') as file:
    file.write(decrypt(key, file_to_decrypt))

print("File has been decrypted successfully")