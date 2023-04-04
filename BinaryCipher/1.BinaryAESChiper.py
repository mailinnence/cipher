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
        if p==0:
            a=b'0###############'+a
        elif p==1:  
            a=b'1###############'+a+b'0'
        elif p==2: 
            a=b'2###############'+a+b'00'
        elif p==3:  
            a=b'3###############'+a+b'000'
        elif p==4:  
            a=b'4###############'+a+b'0000'
        elif p==5:  
            a=b'5###############'+a+b'00000'
        elif p==6:  
            a=b'6###############'+a+b'000000'
        elif p==7:  
            a=b'7###############'+a+b'0000000'
        elif p==8:  
            a=b'8###############'+a+b'00000000'
        elif p==9:    
            a=b'9###############'+a+b'000000000'
        elif p==10: 
            a=b'10##############'+a+b'0000000000'
        elif p==11: 
            a=b'11##############'+a+b'00000000000'
        elif p==12: 
            a=b'12##############'+a+b'000000000000'
        elif p==13: 
            a=b'13##############'+a+b'0000000000000'
        elif p==14: 
            a=b'14##############'+a+b'00000000000000'
        elif p==15: 
            a=b'15##############'+a+b'000000000000000'        
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
    with open("C:\\Users\\", "wb") as f:
        f.write(ciphered)
        f.close() 

        
        
        
def read():
    keytext ='a1a1a1a1a1'
    ivtext=''   
    myCipher = myAES(keytext, ivtext)
    with open("C:\\Users\\", "rb") as f:
        deciphered = myCipher.dec(f.read())
        f.close()    
    with open("C:\\Users\\", "wb") as f:
        f.write(deciphered)
        f.close()      
     
     
if __name__=='__main__':             
  write()     
  read()     
