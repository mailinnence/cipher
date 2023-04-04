from Crypto.Cipher import AES
from Crypto.Hash import SHA256 as SHA
import sys
from datetime import datetime
import tkinter
import os
import moviepy.editor as mp
import time
import datetime


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
        


window=tkinter.Tk()
window.title("My Secret Record")
window.geometry("900x620+100+100")
window.resizable(True, True)
class main:
    def __init__(self):
        self.selectNum=2
    def mainpage(self):
        #버튼으로 지우는 함수
        def page1():
            #place 지우는 함수
            fbutton1.pack_forget()
            fbutton2.pack_forget()
            #pack 지우는 함수
            marginOne1.pack_forget()
            marginOne2.pack_forget()
            marginOne3.pack_forget()
            marginOne4.pack_forget()
            marginOne5.pack_forget()
            marginTwo1.pack_forget()
            marginTwo2.pack_forget()
            marginTwo3.pack_forget()
            page1.pack_forget()
            page2.pack_forget()
            main().page1()
        def page2():
            #place 지우는 함수
            fbutton1.pack_forget()
            fbutton2.pack_forget()
            #pack 지우는 함수
            marginOne1.pack_forget()
            marginOne2.pack_forget()
            marginOne3.pack_forget()
            marginOne4.pack_forget()
            marginOne5.pack_forget()
            marginTwo1.pack_forget()
            marginTwo2.pack_forget()
            marginTwo3.pack_forget()
            page1.pack_forget()
            page2.pack_forget()
            main().page2()
        def openfile(num):
            if os.name == 'nt':
                if num==1:
                    os.startfile('folder1')
                if num==2:
                    os.startfile('folder2')
            else:
                if num==1:
                    os.system('nautilus folder1')
                if num==2:
                    os.system('nautilus folder2')
        #메뉴바 초기화
        menubar=tkinter.Menu(window)
        menu_1=tkinter.Menu(menubar, tearoff=0)
        window.config(menu=menubar)
        #한칸띄우기 용 위젯
        marginTwo1=tkinter.Label(window, height=10)
        marginTwo2=tkinter.Label(window, width=10 )
        marginTwo3=tkinter.Label(window, width=10 )
        marginTwo1.pack()
        #메인 테마 라벨
        marginOne1=tkinter.Label(window, text="AES")
        marginOne1.configure(font=("", 40, ""))
        marginOne1.pack()
        #plaintext
        marginOne2=tkinter.Label(window, height=5 ,text="My Secret Record")
        marginOne2.configure(font=("", 16, ""))
        marginOne2.pack()
        #mp3 전환 페이지로 이동
        fbutton1 = tkinter.Button(window, width=15 , text="Before AES" , command=page1 )
        fbutton1.configure(font=("", 16, ""))
        marginTwo2.pack(side="left")
        fbutton1.pack(side="left")
        #mp3 분리 페이지로 이동
        fbutton2 = tkinter.Button(window, width=15 , text="After AES", command=page2  )
        fbutton2.configure(font=("", 16, ""))
        marginTwo3.pack(side="right")
        fbutton2.pack(side="right")
        #한칸 내리기
        marginOne3=tkinter.Label(window, height=8)
        marginOne3.pack()
        #convert 리스트를 보여줌
        page1= tkinter.Button(window, width=18 , text="Before AES",command=lambda: openfile(1) )
        page1.configure(font=("", 16, ""))
        page1.pack()
        #한칸 내리기
        marginOne4=tkinter.Label(window)
        marginOne4.pack()
        #mp3 리스트를 보여줌
        page2= tkinter.Button(window, width=15 , text="After AES",command=lambda: openfile(2) )
        page2.configure(font=("", 16, ""))
        page2.pack()
        #한칸 내리기
        marginOne5=tkinter.Label(window)
        marginOne5.pack()
   
        window.mainloop()
        
        
    def page1(self):
        def movemainpage():
            marginTwo1.pack_forget()
            mp4list.pack_forget()
            plaintext1.pack_forget()
            actionbutton.pack_forget()
            showfolder1filebutton1.pack_forget()
            showfolder1filebutton2.pack_forget()
            marginOne1.pack_forget()
            marginOne2.pack_forget()
            marginOne3.pack_forget()
            marginOne4.pack_forget()
            marginOne5.pack_forget()
            marginOne6.pack_forget()
            marginOne8.pack_forget()
            ivtextinput.pack_forget()
            main().mainpage()
        def openfile(num):
            if os.name == 'nt':
                if num==1:
                    os.startfile('folder1')
                if num==2:
                    os.startfile('folder2')
            else:
                if num==1:
                    os.system('nautilus folder1')
                if num==2:
                    os.system('nautilus folder2')
        def action(arg):
            try:
                path = os.getcwd()
                file_names = os.listdir(file_path)
                file_names
                for name in file_names:
                    #print(path+"\\folder1\\"+name )
                    keytext =''
                    ivtext=arg
                    with open(path+"\\folder1\\"+name , "rb") as f:
                        a=f.read()
                        f.close()
                        myCipher = myAES(keytext, ivtext)
                        ciphered = myCipher.enc(a)
                        now = datetime.datetime.now()   
                        time="-"+str(now.hour)+"-"+str(now.minute)+"-"+str(now.second)+"-"+str(now.microsecond)
                        now = str(now)
                        now2=now.split(' ')
                        f.close() 
                        now3 = now2[1].split(':')
                    with open(path+"\\folder2\\"+now2[0]+time+ ".bin", "wb") as f:
                        f.write(ciphered)
                        f.close() 
                        os.system("del "+path+"\\folder1\\"+name)
                marginOne6['text']="Complete!!"
            except:
                marginOne6['text']="error"
        #메뉴바 설정
        menubar=tkinter.Menu(window)
        menu_3=tkinter.Menu(menubar, tearoff=0)
        menu_3.add_command(label="첫페이지로 돌아가기" ,command=movemainpage)
        menubar.add_cascade(label="끝내기", menu=menu_3)
        window.config(menu=menubar)
        #한칵 띄우기
        marginTwo1=tkinter.Label(window, width=2 )
        marginTwo1.pack(side="left")
        #mp4 파일 리스트 목록
        mp4list=tkinter.Text(window,width=23,height=18)
        mp4list.insert(tkinter.CURRENT, "_<folder List>__________\n")
        file_path = './folder1'
        file_names = os.listdir(file_path)
        file_names
        for name in file_names:
            name2=name.split('.')
            #if name2[1]=="mp4":
            name+="\n"
            mp4list.insert(tkinter.CURRENT, name)
            
        mp4list.configure(font=("", 24, "") , state='disabled')
        mp4list.pack(side="left")
        #한칸 띄우기
        marginOne1=tkinter.Label(window, height="5" )
        marginOne1.pack()
        #설명문
        plaintext1=tkinter.Label(window , text="Enter ivtext and press Encode")
        plaintext1.configure(font=("", 16, ""))
        plaintext1.pack()
        #한칸 띄우기
        marginOne2=tkinter.Label(window )
        marginOne2.pack()
        #ivtext 입력
        ivtextinput=tkinter.Text(window,width=30,height=2,)
        ivtextinput.pack()
        #한칸 띄우기
        marginOne8=tkinter.Label(window)
        marginOne8.pack()        
        #전환 버튼
        actionbutton = tkinter.Button(window, width=15,text="Encode" ,command=lambda:action(ivtextinput.get("1.0","end")))
        actionbutton.configure(font=("", 16, ""))
        actionbutton.pack()
        #한칸 띄우기
        marginOne3=tkinter.Label(window)
        marginOne3.pack()
        #파일열기 버튼
        showfolder1filebutton1 = tkinter.Button(window, width=15,text="Before AES" ,command=lambda: openfile(1))
        showfolder1filebutton1.configure(font=("", 16, ""))
        showfolder1filebutton1.pack()
        #한칸 띄우기
        marginOne4=tkinter.Label(window)
        marginOne4.pack()
        #파일열기 버튼
        showfolder1filebutton2 = tkinter.Button(window, width=15,text="After AES" ,command=lambda: openfile(2))
        showfolder1filebutton2.configure(font=("", 16, ""))
        showfolder1filebutton2.pack()
        #한칸 띄우기
        marginOne5=tkinter.Label(window ,text="")
        marginOne5.pack()
        #예외처리 결과
        marginOne6=tkinter.Label(window ,text="")
        marginOne6.configure(font=("", 16, ""))
        marginOne6.pack()

    
    def page2(self):
        def movemainpage():
            marginTwo1.pack_forget()
            mp4list.pack_forget()
            plaintext1.pack_forget()
            actionbutton.pack_forget()
            showfolder2listbutton.pack_forget()
            showfolder3listbutton.pack_forget()
            marginOne1.pack_forget()
            marginOne2.pack_forget()
            marginOne3.pack_forget()
            marginOne4.pack_forget()
            marginOne5.pack_forget()
            marginOne6.pack_forget()
            marginOne8.pack_forget()
            ivtextinput.pack_forget()
            main().mainpage()
        def openfile(num):
            if os.name == 'nt':
                if num==1:
                    os.startfile('folder1')
                if num==2:
                    os.startfile('folder2')
            else:
                if num==1:
                    os.system('nautilus folder1')
                if num==2:
                    os.system('nautilus folder2')
        def selectNum(num):
            self.selectNum=num
        def action(arg):
            try:
                path = os.getcwd()
                file_names = os.listdir(file_path)
                file_names
                for name in file_names:
                    keytext =''
                    ivtext=arg
                    with open(path+"\\folder2\\"+name , "rb") as f:   
                        myCipher = myAES(keytext, ivtext) 
                        deciphered = myCipher.dec(f.read())
                        f.close()
                        name2=name.split('.')
                    with open(path+"\\folder1\\"+name2[0]+".txt", "wb") as f:
                        f.write(deciphered)
                        f.close() 
                marginOne6['text']="Complete!!"
            except:
                marginOne6['text']="error"
        #메뉴바 설정
        menubar=tkinter.Menu(window)
        menu_3=tkinter.Menu(menubar, tearoff=0)
        menu_3.add_command(label="첫페이지로 돌아가기" ,command=movemainpage)
        menubar.add_cascade(label="끝내기", menu=menu_3)
        window.config(menu=menubar)
        #한칵 띄우기
        marginTwo1=tkinter.Label(window, width=2 )
        marginTwo1.pack(side="left")
        #mp4 파일 리스트 목록
        mp4list=tkinter.Text(window,width=23,height=18)
        mp4list.insert(tkinter.CURRENT, "_<Mp3 List>___________\n")
        file_path = './folder2'
        file_names = os.listdir(file_path)
        file_names
        for name in file_names:
            name+="\n"
            mp4list.insert(tkinter.CURRENT, name)
  
        mp4list.configure(font=("", 24, "") , state='disabled')
        mp4list.pack(side="left")
        #한칸 띄우기
        marginOne1=tkinter.Label(window, height="5" )
        marginOne1.pack()
        #설명문
        plaintext1=tkinter.Label(window , text="Enter ivtext and press Encode")
        plaintext1.configure(font=("", 16, ""))
        plaintext1.pack()
        #한칸 띄우기
        marginOne2=tkinter.Label(window )
        marginOne2.pack()
        #ivtext 입력
        ivtextinput=tkinter.Text(window,width=30,height=2,)
        ivtextinput.pack()
        #한칸 띄우기
        marginOne8=tkinter.Label(window )
        marginOne8.pack()
        #분리 버튼
        actionbutton = tkinter.Button(window, width=15,text="DeCode" ,command=lambda:action(ivtextinput.get("1.0","end")))
        actionbutton.configure(font=("", 16, ""))
        actionbutton.pack()
        #한칸 띄우기
        marginOne3=tkinter.Label(window)
        marginOne3.pack()
        #파일열기 버튼
        showfolder2listbutton = tkinter.Button(window, width=15,text="Before AES" ,command=lambda: openfile(1))
        showfolder2listbutton.configure(font=("", 16, ""))
        showfolder2listbutton.pack()
        #한칸 띄우기
        marginOne4=tkinter.Label(window )
        marginOne4.pack()
        #파일열기 버튼
        showfolder3listbutton = tkinter.Button(window, width=18,text="After AES" ,command=lambda: openfile(2))
        showfolder3listbutton.configure(font=("", 16, ""))
        showfolder3listbutton.pack()
        #한칸 띄우기
        marginOne5=tkinter.Label(window ,text="")
        marginOne5.pack()
        #예외처리 결과
        marginOne6=tkinter.Label(window ,text="")
        marginOne6.configure(font=("", 16, ""))
        marginOne6.pack()



if __name__=='__main__':
    main().mainpage()