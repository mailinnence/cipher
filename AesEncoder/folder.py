import tkinter as tk
from tkinter import filedialog
from Crypto.Cipher import AES
import os
import hashlib

DEFAULT_KEY = 'YourSecretKeyHere'

def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):
    if not out_filename:
        out_filename = in_filename + '.enc'
    iv = os.urandom(16)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(in_filename)
    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(filesize.to_bytes(8, 'big'))
            outfile.write(iv)
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - len(chunk) % 16)
                outfile.write(encryptor.encrypt(chunk))



def decrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]
    with open(in_filename, 'rb') as infile:
        origsize = int.from_bytes(infile.read(8), 'big')
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)
        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(origsize)



def hash_key(key):
    return hashlib.sha256(key.encode('utf-8')).digest()



def select_file():
    filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("All Files", "*.*"),))
    return filename




def encrypt_selected_file():
    key = DEFAULT_KEY
    key = hash_key(key)
    input_file_path = select_file()
    if input_file_path:
        encrypt_file(key, input_file_path)



def decrypt_selected_file():
    key = DEFAULT_KEY
    key = hash_key(key)
    input_file_path = select_file()
    if input_file_path and input_file_path.endswith('.enc'):
        decrypt_file(key, input_file_path)



# GUI 생성
root = tk.Tk()
root.title("File Encryption")

# 암호화 버튼
encrypt_button = tk.Button(root, text="Encrypt File", command=encrypt_selected_file, width=20, height=2)
encrypt_button.pack(pady=10)  # 버튼과 다음 위젯 사이의 간격 조정

# 복호화 버튼
decrypt_button = tk.Button(root, text="Decrypt File", command=decrypt_selected_file, width=20, height=2)
decrypt_button.pack(pady=10)  # 버튼과 다음 위젯 사이의 간격 조정

root.geometry("300x150")  # 윈도우 크기 설정 (가로x세로)
root.mainloop()
