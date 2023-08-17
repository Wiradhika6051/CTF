## Challenge Name: Imported
>Category: Reverse Engineering

>Points: 454

>Solves: 17

### Challenge Description: 

Author: rorre

I learned how to do dynamic import! It's so cool!

Artifact Files:
* [decode.py](https://ctf.compfest.id/files/fc46c1ca76a2ceec928a0861dfd31d6f/decode.py?token=eyJ1c2VyX2lkIjoxMCwidGVhbV9pZCI6bnVsbCwiZmlsZV9pZCI6MjF9.ZN3zNA.ZwTDlZQBJ1-TrNDScdIfaoSs5g0)
* [secret.py](https://ctf.compfest.id/files/74f9d3847b81d74e183b89f6ff9caf4f/secret.py?token=eyJ1c2VyX2lkIjoxMCwidGVhbV9pZCI6bnVsbCwiZmlsZV9pZCI6MjJ9.ZN3zNA.K4dIlYMDru2yl8ow6jQugyKW7lI)

### Approach

**1. Analyze ```secret.py```**

Pertama kita lihat dulu file ini.
```
import hashlib
import base64
import zlib


def update():
    data = "eJw0mbdu7FyWRvP/KS4mmgEDetfABEVT9N4zo/fe8+m7LhqtSIKAqjqHe3/fWlIzzNO6/6mTre6b9J/mPz+myVYQ2H9/ev/+5p9/8qL8c8x5shf/+3//+ufP7+v3ffLn///8TyFf0EAVBnHNiF2Up/JgVDJpHD44FYPdzTuOwqgY0UnicJrWwuwsH37rX7rH1WVYxTgnERNCiTSKEIAo6RPLY6CBZNKkyjOkQYqiQNsfaSOOGjTbQbAsQdA0RxoMSfNEX/IFQd+ZQl0k1ApjS5jtVkjKy0QIwCMhh9Ace6q+pdwXHetGsokNi8NVoV4RZ1dhFKcudKeAINb+xCOFxF7/YfhiY1HsJZXFEgKjFiqPif3TJD6zfBmCFVfFx6iMD35aLAYxhoQdH7VqsdumElEU7xBGuC+3R3fT8rwyHgvTLOA8GcWuq4wlLFWlZdZtf4PfBJNVJsJ5D9g9tHkLKCu3lUJoBf6m3puPpX5dfmJo6No9WyJ6MqOWGHMptXw
    .....
    4AgGC3gmVJwCWIN0m5ghQwmtpBgyUpgWgqmClxFsyJovdb7IFHI6nsPU+vUyZAMuDPpR4YtEzwcz5gj4vVf/7zz3/89b6uZq//muZi/Nf//E/Z9MX//M//+uufV/rPv/9Ktr/K//3fff68yn9fa7MX/3r6Jv13XmTTMK/Ftv0rTbYC//w7xT9/NubFv/JkT/7+++//HphsW7Huf9XJVv85bKsTBMP/u8e/i/G/e//997/r4pc3VbHt//r7r//8569/Zh8YyRLog3xygoTzEsLw8iU1mKIgFEEQGMfLBC3ID5YTCYqXOIJ9kpIiPhScYViKlv/8xz/+kRflX9m//v5/4V/1266/sn9ff/2fvyjq/zfpzxbgP3/B/91wzG9Ybzz/fbMW+7GOf/3zn/803v/3fH92/c9f0D/+L4dOVQk="
    with open(__file__, "wb") as f:
        f.write(zlib.decompress(base64.b64decode(data)))
    assert hashlib.sha256(data.encode()).hexdigest() == "44e33d3e735456b2559af6236397182aa776d9c6f0b84504cbc8ba5452b121fa"


def c():
    while c.w < 9:
        c.w += 1
    update()
    return """C"""


c.w = 0
```
File ini berisi sebuah variabel bernama ```c.w``` yang diinisialisasi dengan nilai 0, fungsi ```c()```, serta fungsi ```update()```.

Fungsi ```c()``` akan melakukan inkremen ```c.w``` sampai nilainya **9**, lalu memanggil fungsi ```update()``` dan mengembalikan string ```C```.

Fungsi ```update()``` memliki sebuah variabel bernama ```data``` yang berisi hasil encoding Base64 yang sangat panjang. Setelah ```data``` diinisialisasi, program akan membuka file ```secret.py``` itu sendiri dan menulis ulang isinya dengan nilai ```data``` yang telah di-_decode_ dan di-_decompress_. Terakhir, dilakukan pemastian bahwa nilai hash data sama dengan sebuah konstanta.

**2. Analisa File ```decode.py```**

Mari kita lihat isi file ```decode.py```:
```
import importlib

module = importlib.import_module("secret")
output = ""

# while True:
while True:
    importlib.reload(module)
    char = module.c()
    output += char
    print(".", end="", flush=True)
    if char == "}":
        print()
        break

print(output)

```
Fungsi ini diawali dengan melakukan import file ```secret.py``` dan hasil import-_nya_ disimpan ke file ```module```. Kemudian, dilakukan inisialisasi variabel ```output```.

Bagian selanjutny adalah alur utama program, yakni infinite loop. Di tiap iterasi, program memuat ulang file ```secret.py``` lalu memanggil fungsi ```c()``` yang ada di file ```secret.py``` dan menyimpan hasil pemanggilan di variabel ```char```. Kemudian, program mencetak ```.``` ke layar.

Jika ```char``` adalah karakter ```}```, maka loop berhenti dan ```output akan dicetak ke layar```.

**3. Find the Exploit**

Langkah pertama untuk mencari celah adalah mencari tahu apa yang terjadi di iterasi pertama. Mari kita modifikasi kode agar hanya melakukan iterasi sekali:
```
import importlib

module = importlib.import_module("secret")
output = ""

# while True:
while True:
    importlib.reload(module)
    char = module.c()
    output += char
    print(".", end="", flush=True)
    break
    if char == "}":
        print()
        break

print(output)
```
Lalu kita jalankan:
```
.C
```
Terlihat bahwa hasil return ```c()``` tercetak. Karena kita tahu file ```secret.py``` akan ter-_update_ pada saat pemanggilan fungsi ```c()```, mari kita lihat isinya sekarang:
```
import hashlib
import base64
import zlib


def update():
    data = "eJw0m8eO6wp2RefvKy48aoMD5mSgB4xiznnGnKOYv751bbhGpSqAEslz9l5LqmrHZd72P036bYY2+6f9v4dZ+i0J7P8fvX9/888/RVn9OZYi3ct//ff//PPn9/X7Pv3z7z//VSoXNH6Lg4Cf1Ckr0IdfaGW/ua7mXPnl8hxIdVHSQx2coCXeuTL0lKHpTKBKSheNSe00CRAZn82ZUlABEesC34z7KqQGWOhGgUBZVvP6ApJwOGQZgeAOgOA5vQC40BOI4uALgj4xR8aHHHxX12DFDtYxijEEKnuy/N44Dpiu2i6svoT7pinOwg4wKzFKzPApUD1gzlKX5OXUcny4hII0my0szx2qTbaZMDcZtg9+h9TcNhI9n1DRJpWlugz8kNcrzjVlhGOUzp6UQFlCPAf32uspgtE1/iJgsyLsR2q6eiQS+Yhh3iwXSqdk97P1xYFbacPa3HWDylwloxJ/
    .....
    72ienXo5L1JYH7RsJQyg2Eoc28stvwUJXrpKmgfLSLP4KxhXrt3P9dNNh389JAganNBVOQgt72lo8GyAGV9gcEKp/Hg7zBl7ACbAPPyOZuBA67icEPigG0/roDTIYIIaIEFRFNjkGbYcjUNLdIExIPilYfS1wf/55z/+erez3qq/xikf/vU//1PUXf4///O//vrnmfzz77/i9a/if/+3zJ+t+Pe51Fv+r9fIJv/O8nTspyVf138l8ZoT2L8TAvuzM8v/lcVb/Pfff/+3Yryu+bL9VcVr9afaWsUITvy3xL/z4b+l//7731V+ZXWZr9u//v7rP//5658IQeIkhNIZgcZkgcQQiqZpCkE0jWNIQb8GN09ICkqgJC5InEqTAskzHMXJhH4xj4L/+Y9//CPLi7/Sf/39/5p/Vm+//kr/ff71f/6iafr/9+nPLuA/f8H/3bFPb7veBv33y5Jv+zL89c9//lN9P+8B/xT9z1/QP/4vz/l6Gg=="
    with open(__file__, "wb") as f:
        f.write(zlib.decompress(base64.b64decode(data)))
    assert hashlib.sha256(data.encode()).hexdigest() == "c412ca0424d781df056f39c19903222166fa3e845d7a36f6254af97491c55b3f"


def c():
    while c.w < 99:
        c.w += 1
    update()
    return """O"""


c.w = 0
```
Terlihat bahwa nilai ```data``` berbeda, nilai ```hash``` yang dicek berubah, serta kondisi di ```while``` loop naik menjadi **99**. Selain itu, string yang dikembalikan sekarang menjadi ```O```.

Karena kita tahu bahwa dua karakter awal flag adalah ```CO```, maka untuk mendapatkan flag nya kita tinggal lanjutkan proses saja. Manual kelar lah ya.

Masalahnya satu, tiap penambahan karakter, loop yang diiterasi menjadi banyak. Kalo cuma 1 digit atau 2 digit gak masalah. Lah kalau sampai 20 digit?? Mau ngubah PC jadi pemanggang?

Sepertinya perlu dicari celah supaya iterasinya cepet.

Hmm apa ya, perasaan yang bisa kita input dikit.

Tunggu ku inget sesuatu, jadi ku pernah baca dokumentasi Typescript tentang ```this``` yang mana kalau tidak digunakan dengan benar bisa ngereferensi ke variabel yang salah. Yakni bisa jadi konteks si ```this``` ini bukan refer ke objeknya, tapi ke si objek yang manggil.

Jadi inget, struktur module python sekilas kan kek objek javascript, jangan-jangan bila kita ubah variabel ```c.w``` di file ```decode.py```, variabel ```c.w``` yang dipakai di fungsi ```c()``` ngikut nilai yang kita ubah.

Mari kita coba!

**4. Testing Exploit**

Kita coba modifikasi kode ```decode.py``` menjadi seperti berikut:
```
import importlib

module = importlib.import_module("secret")
output = ""

i = 0
while True:
    importlib.reload(module)
    module.c.w = int("9" * (i+1))
    print("nilai sekarang: ",module.c.w)
    char = module.c()
    output += char
    print(".", end="", flush=True)
    break
    i+=1
    if char == "}":
        print()
        break

print(output)
```
Supaya loop nya ke bypass, kita assign nilai ```c.w.``` dengan nilai ```9``` sebanyak jumlah iterasi. Lalu kita print nilainya untuk memastikan.

Mari kita modifikasi sedikit file ```secret.py```. Jangan lupa undo agar kembali ke keadaan awal sebelum diubah yang bisa dilakukan dengan ```ctrl+z```:
```
.....
   sn9ff/2fvyjq/zfpzxbgP3/B/91wzG9Ybzz/fbMW+7GOf/3zn/803v/3fH92/c9f0D/+L4dOVQk="
   with open(__file__, "wb") as f:
        f.write(zlib.decompress(base64.b64decode(data)))
   assert hashlib.sha256(data.encode()).hexdigest() == "44e33d3e735456b2559af6236397182aa776d9c6f0b84504cbc8ba5452b121fa"


def c():
    print("di secret.py: ",c.w)
    while c.w < 9:
        c.w += 1
    update()
    return """C"""


c.w = 0
```
Sekarang coba kita jalankan.
```
nilai sekarang:  9
di secret.py:  9
.C
```
Alhamdulillah keganti. Berarti bener dugaan kita. Sekarang saatnya mendapatkan flag.

**5. Get the Flag**

Kita reset usu file ```secret.py``` dengan melakukan undo sampai kembali ke keadaan awal. Kemudian lakukan modifikasi di file ```decode.py```:
```
import importlib

module = importlib.import_module("secret")
output = ""

i = 0
while True:
    importlib.reload(module)
    module.c.w = int("9" * (i+1))
    char = module.c()
    output += char
    print(".", end="", flush=True)
    i+=1
    if char == "}":
        print()
        break

print(output)
```
Kodenya mirip seperti sebelumnya, namun sekarang kita buat agar bisa berjalan hingga mencapai karakter terakhir flag.

Sekarang mari kita jalankan:
```
..............................................................................................................................................................................
COMPFEST15{dyN4Mic_1mP0rt_1S_m4g1c_6f26bcda30cd85513cba3db0a5f8f16f_abcbaf39b912e3436a7d3a35c33a9f2e865a4fda_ec7e3d57d68307470805a9a4c1eb101cc2f1acc2de094d58e08b8a2d3b9f7eef}
```
Alhamdulillah dapat flag-nya:
```
COMPFEST15{dyN4Mic_1mP0rt_1S_m4g1c_6f26bcda30cd85513cba3db0a5f8f16f_abcbaf39b912e3436a7d3a35c33a9f2e865a4fda_ec7e3d57d68307470805a9a4c1eb101cc2f1acc2de094d58e08b8a2d3b9f7eef}
```

**6. BONUS POINT**

Jika sudah mendapatkan flag, isi file ```secret.py``` akan menjadi berikut:
```

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⢆⡱⢫⡟⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⢿⣻⢿⣟⡿⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠠⠀⢂⡘⢦⡳⣏⣾⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣞⣿⣳⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠐⠈⣌⢣⡑⢦⣙⢮⣳⢻⡾⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣾⢷⣿⢯⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣌⡳⢈⡒⡌⡖⣭⢺⡭⣞⡥⣏⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣟⡾⣏⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⡈⢑⡣⢜⡜⡱⣌⢧⡽⣲⣽⢻⣾⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣽⣻⡽⣷⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠁⠂⠐⢈⠐⡡⠊⢎⡳⣟⠾⣝⡾⣛⣾⢳⢯⡻⡝⣯⢟⡿⣻⢿⣟⡿⣟⣿⢻⠿⡿⣿⢿⡿⣿⣿⢿⣾⣿⣿⣷⡿⣽⣳⠭⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠐⣸⢮⣷⡱⣭⣞⡵⣏⢿⡱⣏⠷⣎⣟⢮⢳⡙⡴⢋⡴⢩⠞⡼⡙⢮⠘⣉⠣⡙⠤⢋⡹⢱⠫⣟⢿⣽⣿⣟⣿⣯⣟⡷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠂⢭⣻⣽⣿⡷⣯⢻⣜⣣⢟⣼⡻⣝⣮⣛⢦⡙⡖⢣⠜⣡⠚⡔⣩⠂⢇⢢⠱⡱⢌⡒⠤⡃⠵⣈⠞⣽⣾⣿⣿⣽⣯⠷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠠⣈⣶⣽⣾⡿⣽⢏⡷⣎⢷⣫⠾⣽⣹⢶⡹⣎⡵⣍⢳⢪⢅⡫⠴⣡⢋⡜⢢⢣⡑⢎⡸⢐⡉⢖⡡⢚⡜⣯⣿⣿⣯⣟⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⡸⣟⣿⡿⣽⣻⢎⣷⡹⣎⣷⣛⣧⢯⣗⡻⣜⡞⣬⢇⡳⢊⡕⢣⢆⢣⠜⣡⠆⡍⢦⠡⠣⠜⢢⡑⢣⢜⣱⢯⣿⢿⡽⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣁⢷⣻⣯⢿⣯⢷⣛⠶⣝⣳⢾⣹⢮⢷⡺⣝⢧⡻⣔⢫⡔⢫⠜⡡⢎⢎⡜⢢⡙⡜⠤⢋⡅⣋⠦⡙⢆⢮⡹⣟⣾⣿⡻⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠰⢬⢏⣷⡿⣟⣮⢳⣭⢻⣭⣟⣯⣿⣯⣿⣷⣯⣿⣳⣮⣳⣜⢣⢎⡱⢎⡖⣸⢡⠚⣄⠫⠔⡘⡔⢢⠍⢎⢲⡹⣽⢾⡷⣟⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡉⢆⢫⣞⢿⡝⣮⢳⢮⣟⣼⢻⣞⡷⢯⡳⣏⢿⡻⣟⡿⣷⢯⣟⣎⠖⣭⢞⡵⣎⡵⣂⠧⣙⠰⣉⠦⡙⡌⢶⣹⢯⣟⣿⡱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡐⢬⢷⡞⣯⡝⣮⢏⣷⣚⣮⢷⣻⣾⣿⣷⣿⣞⣷⣯⣟⣿⣻⡾⣝⠎⡜⢯⡾⣿⣽⢿⣻⣮⢷⡜⣦⣑⢚⢦⣻⣯⡿⣞⠥⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⡄⢫⠞⡑⢊⠱⠉⠞⣲⣛⠾⣏⡿⣹⢾⡹⢣⢏⠾⣽⣻⢾⣽⣻⢭⡚⣌⢣⢛⣷⣯⣿⣧⡝⣎⡝⠶⡭⡞⢦⣻⣯⢿⡉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠰⣎⡷⣞⣧⡚⠀⠀⠀⠀⡘⠴⣩⠿⣜⣳⡱⢎⡵⣋⢮⡟⣷⢯⣟⣾⢣⠷⡱⢌⠦⡙⣎⠿⣹⠻⡟⣷⢾⡱⢣⠝⡲⢯⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢌⣻⣽⣻⡽⣶⡹⠄⠀⢌⠰⣌⡳⣝⣯⢳⡧⣝⣏⢶⡹⣎⡿⣽⣻⢾⣝⡯⢏⡵⢊⠖⡱⢌⡚⢥⠓⡜⢤⠣⡙⢥⢋⡵⣻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⢳⣳⢯⣟⡾⣝⢦⠈⣂⠳⡜⣽⢺⡼⣳⡽⣞⣼⣳⢿⣹⣟⡷⢯⣛⣮⡝⣮⠰⣉⢎⡱⠌⡜⢢⡙⡜⢢⡑⡩⢆⢣⢺⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠡⢏⡿⣾⣽⢫⣮⡑⠤⡛⣼⢣⡯⣗⡯⢷⣛⡾⣽⣞⣷⣻⣾⢿⡿⣷⢿⣞⣳⣵⢪⠴⡩⢜⠡⡒⠌⡥⢒⡱⢊⢆⠯⣼⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠭⢳⢧⣛⡧⣷⣙⢦⡙⣦⢏⡷⣹⢞⡯⣯⣽⢳⣞⡷⣯⣟⣯⠿⣝⠻⡜⡭⠻⣍⠚⡵⣊⠵⣡⢋⡔⢣⠜⣡⠞⡰⢭⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠾⣱⠿⣼⡹⢮⡱⣎⠿⣜⢧⢯⣳⠷⣭⣟⡾⡽⢧⣻⣜⠳⣌⠳⡩⠔⢣⠌⡓⢬⢃⡞⢤⠣⡜⢣⡙⣤⢛⡥⢫⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠠⢉⢧⡳⣭⢻⡜⣯⢞⣵⣻⣳⢯⡾⣽⢯⣷⣞⣷⣬⣳⡹⣌⠣⡜⢱⢊⠖⡸⢂⡳⢌⢣⠜⡰⣋⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡘⢦⡻⣜⢧⣻⡜⣯⢞⡵⣯⣿⣿⣿⣿⣿⣾⣽⣾⣽⣿⣽⣷⣎⡕⡪⢜⡡⢓⡜⡌⢦⡙⡔⠡⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢉⠲⣝⢮⡳⢧⡻⣜⢯⡽⣳⡽⣞⣯⣟⡻⣙⢛⠻⣻⢿⡿⣟⢯⡛⡕⢪⠔⡣⢜⡘⠆⠱⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢪⠔⡹⢮⡝⣧⢻⡜⣧⢻⡵⣛⣾⢳⣯⢷⣹⢮⡗⣧⢛⡼⢌⠦⡑⢮⡑⢎⡱⢊⠔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⢞⡡⣛⡼⣣⢟⡼⣣⠿⣜⠿⣼⣻⣞⣯⢷⣻⣼⢣⢏⡲⣉⠖⡩⢆⡙⢦⠱⡉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢭⡚⣵⢣⡟⣵⢯⣞⡵⣻⢭⡟⡶⣓⠮⡜⢭⡒⣍⠣⢎⠴⡡⢎⡕⢪⡑⢎⡱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⢟⡼⣣⢿⡹⡾⣼⣹⢧⡟⣾⣱⢏⡷⣙⢦⡱⢌⠳⣌⠲⡑⢎⡜⡥⡙⢦⡑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠭⣞⡵⣛⡮⣗⢿⣱⢯⠾⣝⡾⣭⣟⡾⣵⢮⣱⢋⠶⣈⢧⣙⠲⣜⡡⢝⢢⡹⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡹⢎⡷⣫⢷⣹⡞⣧⢟⣻⡽⣽⣳⢯⡿⣽⣞⡷⣯⢻⡭⢶⢩⠓⢦⡙⢬⠲⣑⢻⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢄⠱⣏⡞⣷⢫⣶⢻⡼⣫⣗⢯⡷⣯⠿⣽⠳⢯⡝⣎⢳⡙⢎⡲⡙⢦⡙⢦⡙⠤⠈⣿⣿⣿⣷⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠄⠛⠼⡙⢞⠻⡜⡳⢏⠷⣞⣻⡼⢧⡻⣜⢫⠖⣜⡸⢆⡝⣪⢕⡹⢦⡙⢦⡙⠆⠀⢾⣿⣿⣿⣿⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠌⣀⡾⡀⢄⡀⠀⠀⠀⠈⣈⠀⣈⣟⣧⢻⣌⢳⡚⡴⢣⢏⡼⣡⢎⡵⢪⡱⢣⡝⠠⠀⢺⣿⣿⣿⣿⣿⣿⣿⣿⣭⡳⣖⡤⣄⣠⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠄⡌⠀⠀⠌⢢⣝⣣⠷⣌⢯⡻⣝⢯⣟⢧⡛⣵⣻⣼⡳⣎⢷⣹⢣⠟⣜⡲⡱⢎⡜⣣⢽⡓⠄⠀⠀⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣱⣳⣎⡷⣯⣛⡷⣚⡴⣠⢄⣀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⡔⢤⢃⡜⢤⣉⠒⡀⠀⢈⠜⢤⡿⣜⣯⠽⣎⡳⡭⢞⢮⡳⣙⢾⣳⢯⡿⣽⡺⣵⢫⡟⢦⢳⡙⢮⣜⡷⡋⠔⠀⠀⠀⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣞⣿⣽⣯⣟⡷⣽⡖⣯⢾⣹⣞⣵⣲⢦⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⣄⢢⢵⣸⡼⣧⣻⣜⠧⢦⣉⠀⠀⠰⣈⠲⣟⡹⣎⠿⣼⡹⣝⣫⠶⣍⠧⣻⡽⣯⣟⣷⣻⡵⣻⡜⣯⢇⣿⣳⢏⠇⠡⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣷⣿⣿⣿⣳⣿⡾⣽⣻⣾⣽⣳⢯⣟⡶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⢀⢡⡘⣌⡟⣼⣿⣿⣿⣿⣼⡟⡄⢀⠀⠀⡁⠀⢡⣏⡘⣏⠛⣤⢹⡌⣧⢋⡙⣌⢡⣿⣡⢻⡜⣇⣿⢡⢻⣸⢻⡜⢡⠈⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣿⣿⣿⣿⣿⣿⣏⡟⣧⣼⢹⡟⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠄⢢⡱⣜⣮⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡱⣃⠀⢀⠐⠈⢠⣯⠵⣯⡻⣵⢫⡞⣵⢫⠷⣌⢻⡶⣯⢿⣽⣻⣞⣯⢿⡽⡏⢎⠁⠂⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣷⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⡄⢢⠱⣤⢫⣷⣽⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣛⡄⠀⠀⡌⢀⠰⣏⢿⡱⣟⡼⢧⡻⣜⢯⡳⣌⢳⡿⣽⣻⡾⣷⣻⢾⢏⠓⡁⠂⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⠠⡐⡌⢤⠳⣜⣣⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⡌⠀⠐⢨⠀⡜⣿⣺⢽⣺⡝⣧⣻⠼⣧⣛⠤⣫⣟⣷⢿⡽⡷⢏⠋⠄⠃⢀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⡘⣤⠳⡼⣜⣷⣻⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⢀⠣⡘⢸⣷⢯⣛⡶⣏⠷⣭⢟⡶⢭⣚⣱⢿⣞⢯⠹⡑⠊⠌⠐⠀⠀⠀⠀⠀⠀⠠⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣶⡽⣞⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⢄⠓⡌⢳⣿⢯⣝⠾⣭⣻⢧⣻⡼⢧⡳⠘⡏⠜⢂⠡⠐⠡⠈⠀⠀⠀⠀⠀⠀⠐⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠐⣌⢘⡰⠉⢞⡛⠎⠛⠱⠋⠉⠑⠙⠋⠓⠡⢎⠘⣀⠂⡁⠂⠠⠀⠀⠀⠀⠀⢄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⢡⣂⡶⣤⣳⣼⣟⣶⣳⡾⣴⣦⣤⣤⣖⡴⣎⢧⡛⣤⣒⡄⡁⠀⠀⠀⠀⠀⡈⡔⣋⢟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⢏⡻⠹⣿⠁⠁⠹⠿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣴⣦⣼⣷⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢐⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣷⡔⠀⠀⠀⠀⢁⣰⣎⣴⣈⣦⡑⣬⢡⡉⢌⠈⣁⠫⣙⠹⣋⠟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢻⠟⡝⠀⠀⠀⠀⠀⠿⡿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣷⣾⣾⣾⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⡳⣼⡱⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣧⣾⡔⠈⠀⠄⠀⢀⡸⣄⣄⣊⣄⢂⡡⢉⠜⣩⠋⠟⡛⠟⡿⠿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢞⣵⣳⢏⡷⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡿⢆⠁⠀⠀⠀⠂⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣼⣷⣮⣷⣼⣳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣫⢾⣽⣻⢼⡱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣦⣓⡆⢀⠦⣄⠀⡀⢰⡠⡑⣨⠉⡝⢩⠛⣛⠻⡛⠿⠿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢿⣳⣟⣮⢳⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⡛⢿⣿⣿⣿⣿⣿⣿⣿⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢇⠠⢈⠀⢂⠰⣿⣷⣿⣷⣿⣿⣷⣿⣶⣷⣽⣮⣵⣜⣶⡴⣮⣝⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⢿⡽⣾⡹⢾⣿⣿⣿⣿⣿⣿⡿⢣⣛⠜⡠⢉⠿⣿⣿⣿⣿⣿⡦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡽⣌⠆⡐⢀⡈⠄⠂⠭⡙⢋⠟⡛⢟⠻⢟⠿⢿⠿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⢿⡽⣧⢻⡹⣿⣿⣿⡿⣟⠣⣍⠣⢜⢢⡑⢦⣜⡽⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢆⣠⢀⢀⡈⢤⣷⣯⣿⣮⣷⣮⣷⣬⣮⣤⣳⣌⣦⣱⣊⡵⣩⢟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⢾⣻⣽⢣⡳⡹⢿⡿⣵⢊⡱⢠⡍⢦⣣⣟⡿⣾⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣙⠦⣹⣯⣀⡘⡿⢻⠿⡻⢿⠿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⢿⡽⣾⢯⣗⣯⢯⡝⣆⠳⣜⢧⡟⣷⣻⣾⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣯⡗⣯⣜⣿⣴⣧⣮⣵⣎⡶⣤⣃⣆⢦⡱⣨⢱⡩⢍⣋⢟⡹⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢯⣿⣽⣻⢾⣝⡾⣽⢎⡷⣈⠎⡝⣎⢟⣿⣿⣿⣿⣿⣿⣿⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⡙⣿⢸⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣾⣿⣷⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣞⡷⢯⣟⡾⣽⣳⡟⡶⣥⢚⡘⣤⢋⠾⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⣧⣙⡯⢜⣳⣌⡖⣌⢦⣡⢋⡜⡩⢍⢫⡙⣋⠟⡛⢟⡻⢟⠿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⢷⣯⣟⣳⢎⡳⢧⣏⠿⣽⢖⡯⣞⡶⣍⢏⣿⣿⣿⣿⣿⣿⣿⣿⣧⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠧⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣼⣷⣽⣶⣳⣮⣷⣾⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣾⣽⣻⢮⡱⢫⡜⣹⢎⡽⢺⡵⢻⡜⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢤⡛⣷⢸⡏⣍⢫⠝⣋⠟⡹⢛⠻⡛⢿⠻⠿⢿⠿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢯⣿⡽⣧⣻⡕⣮⡱⢎⡔⢣⢚⡕⢺⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣝⡷⢺⣿⣾⣿⣿⣾⣽⣷⣯⣷⣽⣦⣽⣜⣦⣳⣌⡶⣰⣎⡼⣧⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢯⣿⣽⢯⡷⡙⢦⢻⡜⣬⡓⣎⡜⣣⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀
⠀⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⡼⣯⢹⡟⢿⠻⡟⠿⡿⢿⢿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⢫⣟⡯⣟⢾⡹⣏⠳⣉⠢⡙⡟⣶⡹⢆⡿⣱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀
⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡼⣧⢻⣽⣶⣷⣮⣷⣼⣎⣦⣵⣢⢦⡱⣌⣣⢍⡹⣩⠛⣝⣫⢟⡿⣻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣫⢞⡵⣋⠶⡱⣍⠳⢄⠢⢱⡙⢦⡙⢮⡜⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣖⠀⠀⠀⠀⠀⠀
⠀⠰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣹⢧⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣾⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⡼⣝⢮⡱⢎⡵⣊⡕⣣⢎⡳⣌⢇⠾⣱⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢺⣧⢿⣳⣜⣦⣕⢮⣡⢏⣭⢫⡝⣋⠟⡛⡟⡻⠿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣹⢚⡶⣽⣺⢵⣫⢶⡝⣮⢻⡵⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢆⠀⠀⠀⠀
⠀⠀⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢯⡷⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣷⣿⣴⣫⣼⣍⣟⣿⣻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⢿⣷⡿⣯⢷⣏⢿⣼⣳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀
⠀⠀⠼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢺⣗⣿⣭⣋⣟⣹⢋⡟⡹⢛⡛⣟⠻⡟⢿⠿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣽⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀
⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡽⣾⣽⣿⣿⣿⣿⣿⣾⣿⣷⣿⣼⣷⣿⣮⣷⣵⣦⣧⣝⣮⣝⣯⣻⣽⣻⣟⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀
⠀⠀⡸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣞⡷⣯⢟⡛⣟⠻⣟⠿⡿⢿⢿⡿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠆⠀
⠀⠀⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣺⣽⣻⣿⣿⣾⣿⣾⣿⣽⣾⣶⣳⣭⣾⣴⣣⡽⣌⣯⣹⣙⣏⡻⣝⢯⣛⣿⣻⣟⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀
⠀⠀⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣵⣳⣿⢿⢻⠟⡿⢿⠿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄
⠀⢀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣞⡷⣿⣧⣿⣾⣵⣯⣾⣼⣳⣮⣷⣭⢯⣹⣍⣻⣙⡟⣛⡟⣛⢻⡛⡟⢿⡻⣟⠿⣿⢿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢺⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⢻⣞⣿⣦⣳⣴⣦⣵⣬⣖⣭⣞⣭⣏⡿⣹⣛⣟⣻⠻⣟⢻⠟⡿⣻⠿⣟⡿⣟⡿⣿⢿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀
```
Kena rickroll cuy wkwkw

### Reflections

Jujur cukup unik karena solusinya cuma menambahkan dua baris kode wkwkwk, tapi menarik jadi tahu sifat import module di python yang bisa kita ubah nilai variabel di lokal dan pemanggilan fungsi di modul tersebut mengikuti nilai di lokal.
  
---
[Back to home](../Readme.md)
