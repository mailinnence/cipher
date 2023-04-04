import os
import time
import tkinter as tk
import requests
from tkinter import filedialog



class FileEncryptor():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("File Decryption Program Download")
        self.root.geometry("610x90+500+300")
        self.root.resizable(False, False)

        # 다운로드 위치 선택
        self.file_label = tk.Label(self.root, text="다운로드 위치:", font=("Arial", 12))
        self.file_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.file_text = tk.Text(self.root, width=30, height=1, font=("Arial", 12), state='disabled')
        self.file_text.grid(row=0, column=1, padx=10, pady=10)

        self.file_button = tk.Button(self.root, text="Select", font=("Arial", 12), command=self.select_file)
        self.file_button.grid(row=0, column=2, padx=10, pady=10)

        self.download = tk.Button(self.root, text="download", font=("Arial", 12), command=self.download)
        self.download.grid(row=0, column=3, padx=10, pady=10)

        self.exceptlabel = tk.Label(self.root, text="다운로드할 위치를 선택해주세요.", font=("Arial", 12))
        self.exceptlabel.grid(row=3, column=1, padx=10, pady=0, sticky=tk.W)

        self.root.mainloop()

    def replace_slash(path):
        return path.replace("/", "\\\\")   

    def replace_slash2(path):
        return path.replace("/", "\\") 
         
    def select_file(self):
        self.filename = filedialog.askdirectory(initialdir="/", title="Select directory")
        self.file_text.config(state='normal')
        self.file_text.delete('1.0', tk.END)
        self.file_text.insert(tk.END, self.filename)
        self.file_text.config(state='disabled')

        
    def download(self):
        if self.file_text.get("1.0", "end-1c") == "":
            self.exceptlabel.config(text="다운로드할 위치가 없습니다.")
        else:
            if os.path.isdir(FileEncryptor.replace_slash(self.file_text.get('1.0','end')[:-1]) + '\\File_Decryption_Program'):
                self.exceptlabel.config(text="이미 설치되어있습니다.")
            else:
                os.mkdir(f"{FileEncryptor.replace_slash(self.file_text.get('1.0','end')[:-1])}\\File_Decryption_Program")
                url = "http://192.168.84.128/index.html"
                response = requests.get(url)

                with open(f"{FileEncryptor.replace_slash2(self.file_text.get('1.0','end')[:-1])}\\File_Decryption_Program\\a.html", "wb") as f:
                    f.write(response.content)

                os.mkdir(f"{FileEncryptor.replace_slash(self.file_text.get('1.0','end')[:-1])}\\File_Decryption_Program\\MyDecFile")
                os.mkdir(f"{FileEncryptor.replace_slash(self.file_text.get('1.0','end')[:-1])}\\File_Decryption_Program\\MyEncFile")

                self.exceptlabel.config(text="설치 완료되었습니다. 5초뒤 자동종료")
                self.root.after(5000, self.root.destroy)



        

FileEncryptor()
