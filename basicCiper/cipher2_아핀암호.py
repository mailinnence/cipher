'''
Created on 2021. 1. 29.

@author: tjdalsdn00
'''

ENC=0
DEC=1
def makeDisk(k1,k2):
    enc_disk={}
    dec_disk={}
    
    for i in range(26):
        enc_i =(k1*i+k2)%26
        enc_ascii = enc_i + 65
        enc_disk[chr(i+65)] = chr(enc_ascii)
        dec_disk[chr(enc_ascii)] = chr(i + 65)

    return enc_disk,dec_disk

def caesar(msg,key1,key2,mode):
    ret=" "
    
    msg=msg.upper()
    enc_disk, dec_disk= makeDisk(key1,key2)
    
    if mode is None:
        return ret
    
    if mode is ENC:
        disk = enc_disk
    if mode is DEC:
        disk = dec_disk
    
    for c in msg:
        if c in disk:
            ret +=disk[c]
        else:
            ret +=c 
        
    return ret 
    
def main():
    plainext ="seong min woo" 
    key ="F"
    
    print("Original:%s" %plainext.upper())
    chi=caesar(plainext,3,4,ENC)
    print("Caesar:%s" %chi)
    decip=caesar(chi,3,4,DEC)
    print("decip:%s" %decip)
    
if __name__=="__main__":
    main()
       











