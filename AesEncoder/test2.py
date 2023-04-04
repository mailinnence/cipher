import os
import time
import tkinter as tk
import requests
from tkinter import filedialog
from Crypto.Cipher import AES
from Crypto.Hash import SHA256 as SHA
import sys
from datetime import datetime
import time


class myAES():
    def __init__(self, keytext, ivtext):
        hash=SHA.new()
        key=hash.digest()
        self.key=key[:16]
        hash.update(ivtext.encode('utf-8'))
        iv=hash.digest()
        self.iv=iv[:16]
    def makeEnabled(self,plaintext):
        fillersize=0
        textsize=len(plaintext)
        if textsize%16 !=0:
            fillersize= 16-textsize%16
        filler='0'*fillersize 
        header='%d'%(fillersize)
        gap=16-len(header)
        header +='#'*gap
        return header+plaintext+filler
    def enc(self, plaintext):
        a=plaintext
        me=sys.getsizeof(a)
        ik=1
        while True:
            if ik-me>=16:
                break
            else:
                ik+=16
        p=int((ik-me)%16) 
        list=[b'0', b'1' , b'2' , b'3' , b'4' , b'5' , b'6' , b'7' , b'8' , b'9' , b'10' , b'11' , b'12' , b'13' ,b'14' , b'15']
        if p<10:
            a=list[p]+b'###############'+a
        else:
            a=list[p]+b'##############'+a
        for i in range(p):
            a+=b'0'
        aes=AES.new(self.key, AES.MODE_CBC,self.iv)
        encmsg=aes.encrypt(a)
        return encmsg
    def dec(self, ciphertext):
        aes=AES.new(self.key, AES.MODE_CBC,self.iv)
        decmsg=aes.decrypt(ciphertext)
        header=decmsg[:16].decode()
        fillersize=int(header.split('#')[0])
        if fillersize !=0:
            decmsg=decmsg[16:-fillersize]
        else:
            decmsg =decmsg[16:]   
        return decmsg
        





class FileEncryptor():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("File Decryption Program")
        self.root.geometry("620x250+500+300")
        self.root.resizable(False, False)


        # 암호화 
        self.enc_label = tk.Label(self.root, text="암호화할 파일:", font=("Arial", 12))
        self.enc_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.enc_loction_text = tk.Text(self.root, width=30, height=1, font=("Arial", 12), state='disabled')
        self.enc_loction_text.grid(row=0, column=1, padx=10, pady=10)

        self.enc_file_button = tk.Button(self.root, text="Select", font=("Arial", 12), command=self.enc_select_file)
        self.enc_file_button.grid(row=0, column=2, padx=10, pady=10)

        self.enc_startbutton = tk.Button(self.root, text="Encryption", font=("Arial", 12), command=self.enc)
        self.enc_startbutton.grid(row=0, column=3, padx=10, pady=10)



        # 복호화 
        self.dec_label = tk.Label(self.root, text="복호화할 파일:", font=("Arial", 12))
        self.dec_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        self.dec_loction_text = tk.Text(self.root, width=30, height=1, font=("Arial", 12), state='disabled')
        self.dec_loction_text.grid(row=1, column=1, padx=10, pady=10)

        self.dec_file_button = tk.Button(self.root, text="Select", font=("Arial", 12), command=self.dec_select_file)
        self.dec_file_button.grid(row=1, column=2, padx=10, pady=10)

        self.dec_startbutton = tk.Button(self.root, text="decryption", font=("Arial", 12), command=self.dec)
        self.dec_startbutton.grid(row=1, column=3, padx=10, pady=10)




        # 키
        self.key_label = tk.Label(self.root, text="암호화 키 :", font=("Arial", 12))
        self.key_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)


        self.key_text = tk.Text(self.root, width=30, height=1, font=("Arial", 12))
        self.key_text.grid(row=2, column=1, padx=10, pady=10)


        # 상황 설명 라벨
        self.exceptlabel = tk.Label(self.root, text=".zip 압축파일만 암호화가 가능합니다", font=("Arial", 12))
        self.exceptlabel.grid(row=3, column=1, padx=10, pady=0, sticky=tk.W)

        self.root.mainloop()


    # 문자열 처리 함수
    def replace_slash(path):
        return path.replace("/", "\\\\")   

    def replace_slash2(path):
        return path.replace("/", "\\") 
         
    # 파일 경로 처리 함수
    def dec_select_file(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select file")
        self.dec_loction_text.config(state='normal')
        self.dec_loction_text.delete('1.0', tk.END)
        self.dec_loction_text.insert(tk.END, self.filename)
        self.dec_loction_text.config(state='disabled')

    def enc_select_file(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select file")
        self.enc_loction_text.config(state='normal')
        self.enc_loction_text.delete('1.0', tk.END)
        self.enc_loction_text.insert(tk.END, self.filename)
        self.enc_loction_text.config(state='disabled')
     


    # 암복호화 함수
    def enc(self):
        try:
            file=FileEncryptor.replace_slash(self.enc_loction_text.get("1.0", "end-1c")).split('\\')
            file_path = os.path.join(os.getcwd(), f"MyEncFile\\{str(datetime.now().strftime('%Y-%m-%d(%H시%M분%S초)'))}{file[-1]}")

            keytext = self.key_text.get("1.0", "end-1c")
            ivtext= self.key_text.get("1.0", "end-1c")
            
            if os.path.isdir(os.path.join(os.getcwd(), "MyEncFile"))==False :
                os.mkdir(os.path.join(os.getcwd(), 'MyEncFile'))

            with open(FileEncryptor.replace_slash(self.enc_loction_text.get("1.0", "end-1c")), "rb") as f:
                a=f.read()
                f.close()
            myCipher = myAES(keytext, ivtext)
            ciphered = myCipher.enc(a)

            with open(file_path, "wb") as f:
                f.write(ciphered)
                f.close() 
            self.exceptlabel.config(text="파일이 암호화 되었습니다")
            self.enc_loction_text.config(state='normal')
            self.enc_loction_text.delete('1.0', tk.END)
            self.enc_loction_text.config(state='disabled')
        except:
            self.exceptlabel.config(text="암호화 할 파일을 선택해주세요")


    def dec(self):
        try:            
            file=FileEncryptor.replace_slash(self.dec_loction_text.get("1.0", "end-1c")).split('\\')
            file_path = (os.path.join(os.getcwd(), f"MyDecFile\\{file[-1]}"))
            keytext = self.key_text.get("1.0", "end-1c")
            ivtext= self.key_text.get("1.0", "end-1c")
            
            if os.path.isdir(os.path.join(os.getcwd(), "MyDecFile"))==False :
                os.mkdir(os.path.join(os.getcwd(), 'MyDecFile'))


            with open(FileEncryptor.replace_slash(self.dec_loction_text.get("1.0", "end-1c")), "rb") as f:
                a=f.read()
                f.close()
            myCipher = myAES(keytext, ivtext)
            deciphered = myCipher.dec(a)


            with open(file_path, "wb") as f:
                f.write(deciphered)
                f.close() 
            self.exceptlabel.config(text="파일이 복호화 되었습니다")
            self.dec_loction_text.config(state='normal')
            self.dec_loction_text.delete('1.0', tk.END)
            self.dec_loction_text.config(state='disabled')
        except:
            self.exceptlabel.config(text="복호화 할 파일을 선택해주세요")



FileEncryptor()
