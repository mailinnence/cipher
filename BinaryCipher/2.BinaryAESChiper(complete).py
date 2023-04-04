# 메모리를 너무 많이 잡아 먹기 때문에
# 용량이 어느 정도 있는 파일은 다른 방법을 사용해야 한다.
# pip install pycryptodomex
# python -m install pycrypto


from Crypto.Cipher import AES
from Crypto.Hash import SHA256 as SHA
import sys

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
        
        
 
        
        
        
def write():
    keytext ='a1a1a1a1a1'
    ivtext=''   
    with open("C:\\Users\\", "rb") as f:
        a=f.read()
        f.close()
    myCipher = myAES(keytext, ivtext)
    ciphered = myCipher.enc(a)
    with open("C:\\Users\\maili\\", "wb") as f:
        f.write(ciphered)
        f.close() 




def read():
    keytext ='a1a1a1a1a1'
    ivtext=''   
    myCipher = myAES(keytext, ivtext)
    with open("C:\\Users\\maili\\", "rb") as f:
        deciphered = myCipher.dec(f.read())
        f.close()    
    with open("C:\\Users\\maili\\", "wb") as f:
        f.write(deciphered)
        f.close()      
     
     
if __name__=='__main__':      
    write()     
    read()     
