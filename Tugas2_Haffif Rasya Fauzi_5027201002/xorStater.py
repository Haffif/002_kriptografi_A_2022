#!/usr/bin/env python3

string="label"
integer=13

ubahAscii=[ord(i) for i in string]
xorAscii=[13 ^ j for j in ubahAscii]
xor_string=''.join(chr(k) for k in xorAscii)

flag = "crypto{" + xor_string + "}"

print(flag)

#the flag is crypto{aloha}