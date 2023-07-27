## Challenge Name: Python Wrangling
Category: General
Points: 10
Solves: 99k+

Challenge Description: 
Python scripts are invoked kind of like programs in the Terminal... Can you run 
[this Python script](https://mercury.picoctf.net/static/b351a89e0bc6745b00716849105f87c6/ende.py) using [this password](https://mercury.picoctf.net/static/b351a89e0bc6745b00716849105f87c6/pw.txt) to get [the flag](https://mercury.picoctf.net/static/b351a89e0bc6745b00716849105f87c6/flag.txt.en)?

Artifact Files:
* [Python Script](https://mercury.picoctf.net/static/b351a89e0bc6745b00716849105f87c6/ende.py)
* [Password File](https://mercury.picoctf.net/static/b351a89e0bc6745b00716849105f87c6/pw.txt)
* [Flag file](https://mercury.picoctf.net/static/b351a89e0bc6745b00716849105f87c6/flag.txt.en)

### Approach

**1. Analyze the content**

Download semua artifak lalu kita lihat satu satu. `pw.txt` dan `flag.txt.en` berisi kombinasi angka dan huruf acak, seperti hasil enkripsi. Saatnya kita lihat `ende.py`

```
import sys
import base64
from cryptography.fernet import Fernet



usage_msg = "Usage: "+ sys.argv[0] +" (-e/-d) [file]"
help_msg = usage_msg + "\n" +\
        "Examples:\n" +\
        "  To decrypt a file named 'pole.txt', do: " +\
        "'$ python "+ sys.argv[0] +" -d pole.txt'\n"



if len(sys.argv) < 2 or len(sys.argv) > 4:
    print(usage_msg)
    sys.exit(1)



if sys.argv[1] == "-e":
    if len(sys.argv) < 4:
        sim_sala_bim = input("Please enter the password:")
    else:
        sim_sala_bim = sys.argv[3]

    ssb_b64 = base64.b64encode(sim_sala_bim.encode())
    c = Fernet(ssb_b64)

    with open(sys.argv[2], "rb") as f:
        data = f.read()
        data_c = c.encrypt(data)
        sys.stdout.write(data_c.decode())


elif sys.argv[1] == "-d":
    if len(sys.argv) < 4:
        sim_sala_bim = input("Please enter the password:")
    else:
        sim_sala_bim = sys.argv[3]
```
Sekilas kode python ini berguna untuk melakukan enkripsi/dekripsi, yang menjelaskan kenapa file password dan file seperti hasil enkripsi.
Karena ini masih challenge awal, ku curiga kalau cara ngesoleve nya tinggal menjalankan programnya. Mari kita coba:
```
python ende.py -d flag.txt.en pw.txt
```

hasil:
```
Traceback (most recent call last):
  File "C:\Users\Anugrah  Wiradhika F\Downloads\ende.py", line 44, in <module>
    c = Fernet(ssb_b64)
  File "C:\Users\Anugrah  Wiradhika F\AppData\Local\Programs\Python\Python310\lib\site-packages\cryptography\fernet.py", line 39, in __init__
    raise ValueError(
ValueError: Fernet key must be 32 url-safe base64-encoded bytes.
```
Lah kok gagal!? mari kita coba lihat `pw.txt`:
```
67c6cc9667c6cc9667c6cc9667c6cc96


```
Ternyata karena ada newline makanya gagal. Mari kita input manual tanpa newline:
```
$ python ende.py -d flag.txt.en
Please enter the password:67c6cc9667c6cc9667c6cc9667c6cc96
picoCTF{4p0110_1n_7h3_h0us3_67c6cc96}
```
Alhamdulillah ketemu flagnya. Didapat flagnya:
```
picoCTF{4p0110_1n_7h3_h0us3_67c6cc96}
```

### Reflections
Awalnya ngira bakal rempong cuma karena pointnya rendah dan masih awal awal sepertinya gampang dan ternyata benar. Lumayan  bagus buat belajar tentang dasar nge pass argument ke program via command line.
  

---
[Back to home](../Readme.md)
