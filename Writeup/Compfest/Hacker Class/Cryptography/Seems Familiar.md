## Challenge Name: Seems Familiar
>Category: Cryptography

>Points: 

>Solves: 

### Challenge Description: 

Your friend has developed an AES-based enryption system in his spare time. That system is very limited and only able to use printable characters, and furthermore, two of four of its functions has yet to be fixed. Even though they are broken, he insisted the flag can be acquired through thorough analysis of the encryption itself. Feeling intrigued, you feel like you are able to get the flag.

```nc 34.101.174.85 10000```

Original Author: potsu

Artifact Files:
* [chall.py](https://ctf.compfest.id/files/8241b44ec3103e47586c9e2a9ed066d5/chall.py?token=eyJ1c2VyX2lkIjoxMCwidGVhbV9pZCI6bnVsbCwiZmlsZV9pZCI6MTN9.ZNyinA.TeLI-8eEKs0BTmQ-UpFV-wBhYrE)

### Approach

**1. Analyze the file**

Berikut adalah isi file ```chall.py``` :
```
from ast import Assert
import sys
import os
import binascii
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from secret import FLAG

IV = os.urandom(AES.block_size)
KEY = os.urandom(AES.block_size)

class Unbuffered(object):
    def __init__(self, stream):
        self.stream = stream
    def write(self, data):
        self.stream.write(data)
        self.stream.flush()
    def writelines(self, datas):
        self.stream.writelines(datas)
        self.stream.flush()
    def __getattr__(self, attr):
        return getattr(self.stream, attr)

sys.stdout = Unbuffered(sys.stdout)

def get_flag():
    print("Sorry, the get_flag function is currently broken. Please try something else.")

def encrypt(msg = None):
    if msg == None:
        msg = input("message (in hex) = ")
    assert len(msg) % 2 == 0, f"Invalid Odd-length string of {msg} has been inputted."
    try:
        msg = binascii.unhexlify(msg.encode()) + FLAG
    except:
        raise AssertionError(f"{msg} is not a valid hex representation.")
    enc = AES.new(KEY, AES.MODE_ECB)
    cipher = enc.encrypt(pad(msg, 16))
    print("ciphertext (in hex): " + binascii.hexlify(cipher).decode())

#DEPRECATED
def decrypt():
    print("Sorry, the decrypt function is currently broken. Please try something else.")

def menu():
    print("1. Get encrypted flag")
    print("2. Encrypt a message")
    print("3. Decrypt a message")
    print("4. Exit")

def main():
    try:
        while True:
            menu()
            choice = input("> " )
            if choice == "1":
                get_flag()
            elif (choice == "2"):
                encrypt()
            elif (choice == "3"):
                decrypt()
            elif (choice == "4"):
                print("ending session.")
                break
            else:
                print("invalid input.")
    except Exception as e:
        print(repr(e))

if __name__ == "__main__":
    main()
```
Penjelasan tentang kode soal adalah sebagai berikut:


**2. Craft Payload and Get the Flag**


### Reflections

Permulaan menarik untuk belajar vulnerability RSA yakni bila nilai ```e``` kecil, ```N``` adalah bilangan prima, serta ```p``` dan ```q``` cukup dekat. Selain itu, _challenge_ ini membantu mengasah skill scripting **python** dan **pwntools**
  

---
[Back to home](../Readme.md)

