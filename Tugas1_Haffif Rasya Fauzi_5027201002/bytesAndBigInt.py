#!/usr/bin/env python3

import sys

from Crypto.Util.number import bytes_to_long
from Crypto.Util.number import long_to_bytes

data=11515195063862318899931685488813747395775516287289682636499965282714637259206269
bytes_=long_to_bytes(data)
print(bytes_)

#the flag is crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}