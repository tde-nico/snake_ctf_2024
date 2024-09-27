from Crypto.Cipher import AES
from hashlib import sha256
from pwn import xor

''' /usr/local/lib/python3.12/hashlib.py
sus = sha256

class sha256:
    def __init__(self, *x, **y):
        print("init sha256")
        print("x", x)
        print("y", x)
        self.s = sus(*x, **y)
    def digest(self, *x, **y):
        print("digest sha256")
        print("x", x)
        print("y", x)
        res = self.s.digest()
        print("digest", res)
        return res
'''

key = 'ca11ab1ecafebabe5ca1ab1edeadbeef'
ct = '2ebb08bf2c0ec28948a837e8d9325d40f3076ad244905965f29ceb1db017e7e7d998902f517d5d1c281be07686e0fce848b65ad2c9824650aac696b03ed0732d'
key = bytes.fromhex(key)
ct = bytes.fromhex(ct)
 
h = sha256(b"\x00\x00\x00*").digest()
ct = xor(ct, h)
cipher = AES.new(key, AES.MODE_ECB)
pt = cipher.decrypt(ct)

print(pt)

# snakeCTF{sp33d_0f_pyth0n_&_s1mpl1c1ty_0f_C_abeb7c997b96c718}
