## Challenge Name: Wireshark doo dooo do doo...
>Category: Forensics

>Points: 50

>Solves: 22,610

### Challenge Description: 

Can you find the flag? [shark1.pcapng](https://mercury.picoctf.net/static/b44842413a0834f4a3619e5f5e629d05/shark1.pcapng).

Artifact Files:
* [shark1.pcapng](https://mercury.picoctf.net/static/b44842413a0834f4a3619e5f5e629d05/shark1.pcapng)

### Approach
**1. Analisis Packet**

Untuk mengerjakan _challenge_ ini, kita perlu _install_ [Wireshark](https://www.wireshark.org/). Setelah ter-_install_, buka **Wireshark** dan muat file ``shark1.pcapng`` yang sudah diunduh.
![loaded packet](images/Wireshark%20doo%20dooo%20do%20doo...-1.JPG)

Untuk mencari _flag_-nya, coba kita cari paket yang mengandung _string_ "picoCTF" menggunakan kueri berikut:
```
frame contains "picoCTF"
```
![search result](images/Wireshark%20doo%20dooo%20do%20doo...-2.JPG)
Gak ketemu dong.

**2. Tracing TCP Packet**  
Setelah baca-baca di internet, ada fitur di Wireshark untuk nge-_track_ aliran komunikasi paket dengan protokol TCP dan UDP. Mungkin ini bisa membantu.

Coba yg TCP dulu. Pergi ke **Analyze** > **Follow** > **TCP Stream**
![start tracking TCP](images/Wireshark%20doo%20dooo%20do%20doo...-3.png)
Akan muncul tampilan seperti ini:
![follow](images/Wireshark%20doo%20dooo%20do%20doo...-4.JPG)

Sekarang tinggal kita analisis aja.
Hmm..di _packet_ 0 gak ada yang aneh, cuma autentikasi kerberos biasa. Coba ke paket selanjutnya dengan menekan tombol inkremen nomor paket.
![increment](images/Wireshark%20doo%20dooo%20do%20doo...-5.JPG)

Jika ditekan, maka akan terlihat _packet_ 1
![packet 1](images/Wireshark%20doo%20dooo%20do%20doo...-6.JPG)
Tidak ada yang menarik. Yaudah kita lanjutin aja.

Kita terus inkremen _packet_ sampai dapat _packet_ yang menarik. Pada _packet_ 5, ada sesuatu yang menarik.
![sus packey](images/Wireshark%20doo%20dooo%20do%20doo...-7.JPG)
```
cvpbPGS{c33xno00_1_f33_h_qrnqorrs}
```
Ini kok formatnya seperti _flag_? Apakah ini _flag_ yang dienkripsi?

**3. Decode the Flag**  
Karena kita gak tahu ini enkripsi apaan, kita coba-cobain di [CyberChef](https://gchq.github.io/CyberChef) sampai ketemu.

Setelah dicoba-coba, ternyata ini adalah enkripsi **ROT 13**.
![rot 13 flag](images/Wireshark%20doo%20dooo%20do%20doo...-8.JPG)
Didapat _flag_-nya adalah sebagai berikut:
```
picoCTF{p33kab00_1_s33_u_deadbeef}
```

### Reflections
Permulaan bagus untuk belajar WireShark, meski awalnya sempet ada kebingungan ini harus diapain.
  

---
[Back to home](../Readme.md)
