from Crypto.Util.number import long_to_bytes

e = 3  # encryption key
# n = prime product
# n = p * q
n = 742449129124467073921545687640895127535705902454369756401331
c = 39207274348578481322317340648475596807303160111338236677373  # ciphertext

# http://factordb.com/index.php?query=742449129124467073921545687640895127535705902454369756401331
p = 752708788837165590355094155871
q = 986369682585281993933185289261

# totient function: ϕ(n)=(p−1)(q−1)
phi = (p-1)*(q-1)

# decryption key
# d = e^(-1) MOD phi
d = pow(e, -1, phi)

# pt = c^d MOD n
pt = pow(c, d, n)
flag = long_to_bytes(pt)

print(flag)
