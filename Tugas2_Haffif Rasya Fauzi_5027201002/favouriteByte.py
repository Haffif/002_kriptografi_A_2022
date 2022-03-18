#!/usr/bin/env python3

from pwn import xor

str = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
for i in range(1,256):    
    fav_byte = xor(bytes.fromhex(str),i)
    if b'crypto' in fav_byte:
        print(fav_byte)

#The flag is crypto{0x10_15_my_f4v0ur173_by7e}