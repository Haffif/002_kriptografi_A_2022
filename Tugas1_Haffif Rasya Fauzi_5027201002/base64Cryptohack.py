#!/usr/bin/env python3

import base64
import sys

hex_str="72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
bytes_=bytes.fromhex(hex_str)
flag=base64.b64encode(bytes_)

print(flag)

#the flag is crypto/Base+64+Encoding+is+Web+Safe/