from Crypto.Cipher import DES3
from Crypto.Hash import SHA256 as SHA
class myDES():
    def __init__(self, keytext, ivtext):
        hash=SHA.new()
        hash.update(keytext.encode('utf-8'))
        key=hash.digest()
       
       
        self.key=key[:24]
        hash.update(ivtext.encode('utf-8'))
        iv=hash.digest()
        self.iv=iv[:8]
    
    def enc(self, plaintext):
        plaintext = make8String(plaintext)
        des3 = DES3.new(self.key, DES3.MODE_CBC,self.iv)
        encmsg = des3.encrypt(plaintext.encode())
        return encmsg
    
    def dec(self, ciphertext):
        des3 = DES3.new(self.key, DES3.MODE_CBC,self.iv)
        decmsg = des3.decrypt(ciphertext)
        return decmsg


def make8String(msg):
    msglen = len(msg)
    filler=''
    if msglen%8 != 0:
        filler = '0'*(8 - msglen%8)
    msg += filler
    return msg    



def main():
    keytext ='samsjang'
    ivtext='1234'   
    msg="woossuk study"
    myCipher = myDES(keytext, ivtext)
    ciphered = myCipher.enc(msg)
    deciphered = myCipher.dec(ciphered)
    print('원문:\t%s' %msg)
    print('암호문:\t%s' %ciphered)
    print('복호문:\t%s' %deciphered)
    
if __name__=='__main__':    
    main()
    
    
'''    
그러나 이렇게 할 시 msg 가 8비트로 되어 있지 않으면 오류 가 나오므로 위의 코드들의 주석을 제거하여 실행하여야 한다.
''' 
    





































