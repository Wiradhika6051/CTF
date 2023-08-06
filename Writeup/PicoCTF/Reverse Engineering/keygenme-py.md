## Challenge Name: keygenme-py
>Category: Reverse Engineering

>Points: 30

>Solves: 19k+

### Challenge Description: 

[keygenme-trial.py](https://mercury.picoctf.net/static/0c363291c47477642c72630d68936e50/keygenme-trial.py)

Artifact Files:
* [keygenme-trial.py](https://mercury.picoctf.net/static/0c363291c47477642c72630d68936e50/keygenme-trial.py)

### Approach
**1. Analisis filenya**

Pertama-tama mari kita unduh filenya. Dari ekstensinya jelas python sih.
```
file keygenme-trial.py
```
No Bukti Hoax:
```
keygenme-trial.py: Python script, ASCII text executable, with very long lines (3876)
```

**2. Analisis Kode**

Next kita lihat-lihat isinya.

- Di bagian atas ada deklarasi variabel
```
#============================================================================#
#============================ARCANE CALCULATOR===============================#
#============================================================================#

import hashlib
from cryptography.fernet import Fernet
import base64



# GLOBALS --v
arcane_loop_trial = True
jump_into_full = False
full_version_code = ""

username_trial = "MORTON"
bUsername_trial = b"MORTON"

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial

star_db_trial = {
  "Alpha Centauri": 4.38,
  "Barnard's Star": 5.95,
```
Disini terlihat ada potongan fragmen flag, dari fragmennya sepertinya kita sueuh generate part dynamicnya. Lalu di bawah ada dictionary berisi string nama bintang dan angka (mungkin jaraknya dalam tahun cahaya?)

- Bagian-bagian selanjutnya berisi fungsi-fungsi yang diperlukan. Supaya bisa lebih dipahami dengan terstruktur, mari kita scroll ke bagian paling bawah untuk melihat program utamanya.
```
# Encrypted blob of full version
full_version = \
b"""gAAAAABgT_nv3JrW2AM..."""



# Enter main loop
ui_flow()

if jump_into_full:
    exec(full_version_code)
```
Oh jadi ini yang kata ```file``` tadi ada very long lines. Untuk mempersingkat writeup, bagian ```full_version``` tidak ku tampilkan semua disini. Sepertinya entar bagian ini perlu di-_decrypt_ agar bisa dapat dynamic part-nya. Jika di run program akan masuk ke main loop di ```ui_flow()```, dan bila variabel ```jump_into_full``` nya nanti ```True``` (di deklarasi awal nilainya ```False```), entar string bernama ```full_version_code``` (keknya code full versionnya), akan dijalankan.

- Next mari kita lihat isi ```ui_flow()```:
```
def ui_flow():
    intro_trial()
    while arcane_loop_trial:
        menu_trial()

def intro_trial():
    print("\n===============================================\n\
Welcome to the Arcane Calculator, " + username_trial + "!\n")    
    print("This is the trial version of Arcane Calculator.")
    print("The full version may be purchased in person near\n\
the galactic center of the Milky Way galaxy. \n\
Available while supplies last!\n\
=====================================================\n\n")
```
Intinya bagian ini akan nge print intro program dan melakukan looping menu.

- Next, kita lihat isi menunya.
```
def menu_trial():
    print("___Arcane Calculator___\n\n\
Menu:\n\
(a) Estimate Astral Projection Mana Burn\n\
(b) [LOCKED] Estimate Astral Slingshot Approach Vector\n\
(c) Enter License Key\n\
(d) Exit Arcane Calculator")

    choice = input("What would you like to do, "+ username_trial +" (a/b/c/d)? ")
    
    if not validate_choice(choice):
        print("\n\nInvalid choice!\n\n")
        return
    
    if choice == "a":
        estimate_burn()
    elif choice == "b":
        locked_estimate_vector()
    elif choice == "c":
        enter_license()
    elif choice == "d":
        global arcane_loop_trial
        arcane_loop_trial = False
        print("Bye!")
    else:
        print("That choice is not valid. Please enter a single, valid \
lowercase letter choice (a/b/c/d).")

def validate_choice(menu_choice):
    if menu_choice == "a" or \
       menu_choice == "b" or \
       menu_choice == "c" or \
       menu_choice == "d":
        return True
    else:
        return False
```
Bagian ini menampilkan prompt dan menerima input dari user berupa karakter ```a```/```b```/```c```/```d```, lalu menjalankan fungsi yang sesuai. Mari kita lihat tiap opsi.

1. Jika pengguna memasukkan ```a```, fungsi ```estimate_burn()``` akan dipanggil.
```
def estimate_burn():
  print("\n\nSOL is detected as your nearest star.")
  target_system = input("To which system do you want to travel? ")

  if target_system in star_db_trial:
      ly = star_db_trial[target_system]
      mana_cost_low = ly**2
      mana_cost_high = ly**3
      print("\n"+ target_system +" will cost between "+ str(mana_cost_low) \
+" and "+ str(mana_cost_high) +" stone(s) to project to\n\n")
  else:
      # TODO : could add option to list known stars
      print("\nStar not found.\n\n")
```
Sepertinya fungsi ini hanya berisi logic permainan dimana pengguna memasukkan input nama bintang, terus digitung range nya.

2. Jika pengguna memasukkan ```b```, fungsi ```locked_estimate_vector()``` akan dipanggil.
```
def locked_estimate_vector():
    print("\n\nYou must buy the full version of this software to use this \
feature!\n\n")
```
Sepertinya fitur ini locked di trial version.

3. Jika pengguna memasukkan ```c```, fungsi ```enter_license()``` akan dipanggil. Karena fungsi ini kompleks dan kemungkinan ini jalan menuju flagnya. Kita bahas yang ```d``` dulu.

4. Jika pengguna memasukkan ```d```, maka pengguna akan keluar dari program.

- Dari keempat opsi ini, opsi ```c``` sepertinya jalan menuju flag. Mari kita analisa.
```
def enter_license():
    user_key = input("\nEnter your license key: ")
    user_key = user_key.strip()

    global bUsername_trial
    
    if check_key(user_key, bUsername_trial):
        decrypt_full_version(user_key)
    else:
        print("\nKey is NOT VALID. Check your data entry.\n\n")
```
Di fungsi yang dipanggil bila pengguna memasukkan ```c```, pengguna akan diminta memasukkan lisence key yang kemudian akan distrip dari spasi/tab di ujung kanan dan kirinya. Kemudian, key yang dimasukkan pengguna akan dicek menggunakan fungsi ```check_key()```. Jika sesuai maka full version nya akan di-_decrypt_.

- Mari kita analisis fungsi ```check_key()```.
```
def check_key(key, username_trial):

    global key_full_template_trial

    if len(key) != len(key_full_template_trial):
        return False
    else:
        # Check static base key part --v
        i = 0
        for c in key_part_static1_trial:
            if key[i] != c:
                return False

            i += 1

        # TODO : test performance on toolbox container
        # Check dynamic part --v
        if key[i] != hashlib.sha256(username_trial).hexdigest()[4]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[5]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[3]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[6]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[2]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[7]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[1]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[8]:
            return False



        return True
```
Fungsi ini pertama memastikan bahwa panjang key yang dimasukkan sama dengan ```username_trial```. Pada pemanggilan fungsi ini, ```username_trial``` adalah variabel ```bUsername_trial``` yang bernilai ```b"MORTON"```. Kemudian, akan dilakukan pengecekan key apakah sesuai dengan static part dan beberapa bagian dari hash SHA-256 dari variabel ```username_trial```. Jika ya, maka key valid.

- Jika key valid, maka akan dilakukan proses dekripsi fullversion.
```
def decrypt_full_version(key_str):

    key_base64 = base64.b64encode(key_str.encode())
    f = Fernet(key_base64)

    try:
        with open("keygenme.py", "w") as fout:
          global full_version
          global full_version_code
          full_version_code = f.decrypt(full_version)
          fout.write(full_version_code.decode())
          global arcane_loop_trial
          arcane_loop_trial = False
          global jump_into_full
          jump_into_full = True
          print("\nFull version written to 'keygenme.py'.\n\n"+ \
                 "Exiting trial version...")
    except FileExistsError:
    	sys.stderr.write("Full version of keygenme NOT written to disk, "+ \
	                  "ERROR: 'keygenme.py' file already exists.\n\n"+ \
			  "ADVICE: If this existing file is not valid, "+ \
			  "you may try deleting it and entering the "+ \
			  "license key again. Good luck")
```
Pada bagian ini, key yang diinput user akan di-_encode_ ke BASE64 lalu dibuat kunci cryptography menggunakan ```Fernet```. Program kemudian akan membuat file baru bernama ```keygenme.py``` untuk menyimpan hasil dekripsi program full version.

**3. Get the Flag!**

Dari flow yang sudah dijelaskan, pertama kita perlu mendapatkan keynya. bagian yang lumayan challenging adalah yang bagian pengecekan hash username_trial. Mari kita kerjakan bagian itu dulu.

Buat fungsi baru untuk mendapatkan hashnya.
```
def HACK_getUsernameHash(username_trial):
  print("Username Hash: ",hashlib.sha256(username_trial).hexdigest())
```
Lalu panggil dengan argument ```bUsername_trial``` sebelum pemanggilan ```ui_flow```.
```
# Enter main loop
HACK_getUsernameHash(bUsername_trial)
ui_flow()

if jump_into_full:
    exec(full_version_code)
```
Mari kita jalankan!
```
Username Hash:  281f75c0145b05e6ccbeecc66a61614d8c974c1a49356c118fcbab4735862fea

===============================================      
Welcome to the Arcane Calculator, MORTON!
...
```
Nah kita dapat hash nya. Sekarang mari kita buat payload key nya. 
1. Fakta Pertama. Panjang kuncinya harus sama dengan ```key_full_template_trial```. Isi ```key_full_template_trial``` adalah:
```
picoCTF{1n_7h3_|<3y_of_xxxxxxxx}
```
Kita jadikan ini sebagai template dulu kali ya.

2. Fakta Kedua. Prefix (awalan) key nya adalah isi variabel ```key_part_static1_trial``` yakni:
```
picoCTF{1n_7h3_|<3y_of_
```

3. Fakta Ketiga. Suffix (akhiran) dari key nya adalah elemen dari hash digest SHA-256 dari ```bUsername_trial``` yang berisi ```b"MORTON"``` dengan indeks secara berurutan:
```
4, 5, 3, 6, 2, 7, 1, 8
```
Karena kita tahu hash SHA-256 ```b"MORTON"```  adalah:
```
281f75c0145b05e6ccbeecc66a61614d8c974c1a49356c118fcbab4735862fea
```
Berikut adalah mapping indeks dan karakternya:
```
4 = '7'
5 = '5'
3 = 'f' 
6 = 'c'
2 = '1' 
7 = '0'
1 = '8'
8 = '1'
```
Diperoleh suffixnya adalah:
```
75fc1081
```
Jangan lupa tambahkan } di akhir agar panjangnya sama dengan key trial.

Jika digabungkan, key nya adalah sebegai berikut:
```
picoCTF{1n_7h3_|<3y_of_75fc1081}
```

Mari kita mulai proses dekripsi!
- Jalankan program.
```
Username Hash:  281f75c0145b05e6ccbeecc66a61614d8c974c1a49356c118fcbab4735862fea

===============================================      
Welcome to the Arcane Calculator, MORTON!

This is the trial version of Arcane Calculator.      
The full version may be purchased in person near     
the galactic center of the Milky Way galaxy.
Available while supplies last!
=====================================================


___Arcane Calculator___

Menu:
(a) Estimate Astral Projection Mana Burn
(b) [LOCKED] Estimate Astral Slingshot Approach Vector
(c) Enter License Key
(d) Exit Arcane Calculator
What would you like to do, MORTON (a/b/c/d)?
```
Masukkan ```c```
```
What would you like to do, MORTON (a/b/c/d)? c

Enter your license key:
```
Masukkan key yang sudah dibuat tadi:
```
Enter your license key: picoCTF{1n_7h3_|<3y_of_75fc1081}

Full version written to 'keygenme.py'.

Exiting trial version...

===================================================

Welcome to the Arcane Calculator, tron!

===================================================


___Arcane Calculator___

Menu:
(a) Estimate Astral Projection Mana Burn
(b) Estimate Astral Slingshot Approach Vector
(c) Exit Arcane Calculator
What would you like to do, tron (a/b/c)?

```
Woah benar dong. Dan jika kamu perhatikan. Akan ada file baru namanya ```keygenme.py```. Namun tidak ada yang spesial di sini , hanya program biasa serta tidak ada kode yang berhubungan dengan flag. Selain itu, karena key nya tadi memiliki pola ```picoCTF{.*}```, ku curiga itu tadi flagnya dan ketika ku input ternyata bener dong. (Sori lupa ss pas input, tapi kalau kamu ikutin cara ini harusnya bakal ada tulisan success sih pas submit).

Jadi flagnya adalah:
```
picoCTF{1n_7h3_|<3y_of_75fc1081}
```
### Reflections
Lumayan menarik bener-bener belajar nge-reverse buat dapetin input yang bener. (Belajar jadi cracker game bajakan moment).

---
[Back to home](../Readme.md)
