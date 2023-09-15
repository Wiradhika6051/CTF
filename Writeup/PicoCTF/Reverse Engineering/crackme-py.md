## Challenge Name: crackme-py
>Category: Reverse Engineering

>Points: 30

>Solves: 28,988

### Challenge Description: 

[crackme.py](https://mercury.picoctf.net/static/f440bf2510a28914afae2947749f2db0/crackme.py)

Artifact Files:
* [crackme.py](https://mercury.picoctf.net/static/f440bf2510a28914afae2947749f2db0/crackme.py)

### Approach
**1. Analisis Program**

Pertama-tama mari kita unduh filenya. Lalu kita buka:
```
# Hiding this really important number in an obscure piece of code is brilliant!
# AND it's encrypted!
# We want our biggest client to know his information is safe with us.
bezos_cc_secret = "A:4@r%uL`M-^M0c0AbcM-MFE0g4dd`_cgN"

# Reference alphabet
alphabet = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"



def decode_secret(secret):
    """ROT47 decode

    NOTE: encode and decode are the same operation in the ROT cipher family.
    """

    # Encryption key
    rotate_const = 47

    # Storage for decoded secret
    decoded = ""

    # decode loop
    for c in secret:
        index = alphabet.find(c)
        original_index = (index + rotate_const) % len(alphabet)
        decoded = decoded + alphabet[original_index]

    print(decoded)



def choose_greatest():
    """Echo the largest of the two numbers given by the user to the program

    Warning: this function was written quickly and needs proper error handling
    """

    user_value_1 = input("What's your first number? ")
    user_value_2 = input("What's your second number? ")
    greatest_value = user_value_1 # need a value to return if 1 & 2 are equal

    if user_value_1 > user_value_2:
        greatest_value = user_value_1
    elif user_value_1 < user_value_2:
        greatest_value = user_value_2

    print( "The number with largest positive magnitude is "
        + str(greatest_value) )



choose_greatest()
```
Di program ini ada fungsi untuk decode secret namun tidak pernah dipanggil.

**2. Mendapatkan Flag**

Untuk memanggil fungsi tersebut tinggal tambahkan saja kode pemanggilannya seperti berikut:
```
decode_secret(bezos_cc_secret)
```
Lalu jalankan ulang. Didapat:
```
picoCTF{1|\/|_4_p34|\|ut_8c551048}
None
What's your first number?
```

Jadi flagnya adalah:
```
picoCTF{1|\/|_4_p34|\|ut_8c551048}
```
### Reflections

Jujur rada _unexpected_ ternyata solusinya tinggal manggil fungsinya doang :pepega:

---
[Back to home](../Readme.md)
