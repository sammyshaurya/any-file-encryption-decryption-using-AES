from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import filedialog
import os

def encrypt_data(key, data):
        try:
            cipher = Fernet(key)
            encrypted_file = cipher.encrypt(data)
            return encrypted_file
        except Exception as e:
            print(f'Error in encrytion: {e}')
            exit()
            
def decrypt(key, data):
        try:
            cipher = Fernet(key)
            decrypted = cipher.decrypt(data)
            return decrypted
        except Exception as e:
            print(f"Error during decryption: {e}")
            exit()

def select_file():
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        return file_path

def go_encrypt():
    # create key
    key = Fernet.generate_key()
    # select file
    
    selected_file = select_file()
    if not selected_file:
        print("No file selected")
        exit()

    with open(selected_file, 'rb') as file:
        data_to_encrypt = file.read()
        encrypted = encrypt_data(key, data_to_encrypt)

    file_base_name = os.path.basename(selected_file)

    encrypted_file_path = file_base_name + '.enc'
    with open(encrypted_file_path, 'wb') as file:
        file.write(encrypted)

    with open(file_base_name + '.key', 'wb') as file:
        file.write(key)

    print(f"Encryption successful. Encrypted file: '{encrypted_file_path}', Key file: '{file_base_name}'.")

def go_decrypt():
    # select file
    def select_file():
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        return file_path

    selected_file = select_file()
    if not selected_file:
        print("No file selected")
        exit()

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


if __name__ == "__main__":
    print("Select operation to perform:")
    print("> Press 1 for ENCRYPT")
    print("> Press 2 for DECRYPT")

    options = input("Enter either 1 or 2:")
    while options not in ['1', '2']:
        options = input("Enter either 1 or 2:")

    if options == '1':
        go_encrypt()
    else:
        go_decrypt()

    exit()