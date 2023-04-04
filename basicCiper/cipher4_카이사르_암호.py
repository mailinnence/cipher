'''
Created on 2021. 1. 28.

@author: tjdalsdn00
'''

ENC=0
DEC=1
def makeDisk(key):
    keytable =map(lambda x: (chr(x+65),x),range(65))
    
    key2index ={}
    
    for t in keytable:
        alphabet, index = t[0],t[1]
        
        key2index[alphabet]= index
        
    if key in key2index:
        k = key2index[key]
    else:
        return None, None
    
    enc_disk={}
    dec_disk={}
    
    for i in range(26):
        enc_i =(i+k)%26
        enc_ascii = enc_i + 65
        enc_disk[chr(i+65)] = chr(enc_ascii)
        dec_disk[chr(enc_ascii)] = chr(i + 65) 
        
        
        
    return enc_disk,dec_disk

def caesar(msg, key,mode):
    ret=" "
    
    msg=msg.upper()
    enc_disk, dec_disk= makeDisk(key)
    
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
    plainext ="암호화 시킬 문장" 
    key ="F"   
    
    print("평문: %s" %plainext)
    chi=caesar(plainext,key,ENC)
    print("암호문: %s" %chi)
    dechi=caesar(plainext,key,DEC)
    print("복호문: %s" %dechi)
    
  
    
if __name__=="__main__":
    main()
       
                