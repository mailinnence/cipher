
import os
import tkinter as tk


# 라이브러리 자동 설치 ---------------------------------------------
try:
    import Crypto
except ImportError:
    try:
        os.system("pip install pycryptodome")
    except Exception as e:
        pass
else:
    pass
# ------------------------------------------------------------------

from tkinter import filedialog, messagebox
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

filepath = ""  # 파일 경로를 전역 변수로 정의

def get_key(input_key):
    key = input_key
    key = key.ljust(32, ' ')
    return key.encode('utf-8')  # Convert the key to bytes

def open_file_explorer():
    global filepath  # 전역 변수로 선언
    # 파일 탐색기 열기
    filepath = filedialog.askopenfilename()
    filepath = filepath.replace("/", "\\")
    selected_file_label.config(text="선택된 파일: " + filepath)  # 파일 경로를 업데이트

def get_encryption_key():
    encryption_key = entry.get()
    print("입력한 암호화 키:", encryption_key)

def encrypt_file():
    global filepath  # 전역 변수로 선언
    key = get_key(entry.get())
    chunk_size = 64 * 1024  # 64 KB chunks
    try:
        # 파일 확장자를 제거한 파일 이름
        output_file_path = filepath[:filepath.rfind(".")] + ".bin"
        iv = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        with open(filepath, 'rb') as infile:
            with open(output_file_path, 'wb') as outfile:
                outfile.write(iv)
                while True:
                    chunk = infile.read(chunk_size)
                    if len(chunk) == 0:
                        break
                    elif len(chunk) % 16 != 0:
                        # Pad the chunk if its length is not a multiple of 16
                        chunk += b' ' * (16 - len(chunk) % 16)
                    outfile.write(cipher.encrypt(chunk))
        current_file_label.config(text="암호화가 완료되었습니다.")
    except Exception as e:
        current_file_label.config(text="암호화가 완료되었습니다." + str(e))

def decrypt_file():
    global filepath 
    key = get_key(entry.get())
    chunk_size = 64 * 1024  
    try:
        with open(filepath, 'rb') as infile:
            iv = infile.read(16)
            cipher = AES.new(key, AES.MODE_CBC, iv)
            output_file_path = filepath[:filepath.rfind(".")] + ".zip"
            with open(output_file_path, 'wb') as outfile:
                while True:
                    chunk = infile.read(chunk_size)
                    if len(chunk) == 0:
                        break
                    decrypted_chunk = cipher.decrypt(chunk)
                    outfile.write(decrypted_chunk)
                outfile.truncate()
        current_file_label.config(text="복호화가 완료되었습니다.")
    except Exception as e:
        current_file_label.config(text="복호화가 완료되었습니다." + str(e))



# Tkinter 애플리케이션을 생성합니다.
root = tk.Tk()

# 창에 대한 설정을 수행할 수 있습니다.
root.title("File Explorer & Encryption/Decryption")  # 창의 제목 설정

# 창의 크기를 지정합니다.
root.geometry("400x400")  # 가로 400픽셀, 세로 400픽셀 크기로 조절

# 파일 탐색기 열기 버튼 생성
file_explorer_button = tk.Button(root, text="파일 탐색기 열기", command=open_file_explorer)
file_explorer_button.pack(pady=10)

# 선택된 파일 경로를 표시할 텍스트 레이블 생성
selected_file_label = tk.Label(root, text="선택된 파일: ")
selected_file_label.pack(pady=5)

# 암호화 키를 입력할 텍스트 상자 생성
entry_label = tk.Label(root, text="암호화 키를 입력하세요:")
entry_label.pack()

entry = tk.Entry(root, show="*")  # 입력한 텍스트가 * 로 표시되도록 설정
entry.pack(pady=5)

# 암호화 버튼 생성
encrypt_button = tk.Button(root, text="암호화", command=encrypt_file)
encrypt_button.pack(pady=5)

# 복호화 버튼 생성
decrypt_button = tk.Button(root, text="복호화", command=decrypt_file)
decrypt_button.pack(pady=5)


# 선택된 파일 경로를 표시할 텍스트 레이블 생성
current_file_label = tk.Label(root)
current_file_label.pack(pady=5)
 

# 창을 띄웁니다.
root.mainloop()
