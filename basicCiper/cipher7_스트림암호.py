from Crypto.Cipher import ARC4
from Crypto.Hash import SHA256 as SHA

class myARC4():
    def __init__(self,keytext):
        self.key=keytext.encode()
        
    def enc(self,plaintext):
        arc4=ARC4.new(self.key)
        encmsg=arc4.encrypt(plaintext.encode())
        return encmsg

    def dec(self,ciphertext):
        arc4=ARC4.new(self.key)
        decmsg=arc4.decrypt(ciphertext)
        return decmsg

def main():
    keytext ='samsjang'
    msg='python3x'
    myCipher=myARC4(keytext)
    ciphered=myCipher.enc(msg)
    deciphered=myCipher.dec(ciphered)
    print('원문:\t%s' %msg)
    print('암호문:\t%s' %ciphered)
    print('복호문:\t%s' %deciphered)
    
if __name__=='__main__':    
    main()        
















