## Challenge Name: MacroHard WeakEdge
>Category: Forensics

>Points: 60

>Solves: 14,291

### Challenge Description: 

I've hidden a flag in this file. Can you find it? [Forensics is fun.pptm](https://mercury.picoctf.net/static/52da699e0f203321c7c90ab56ea912d8/Forensics%20is%20fun.pptm)

Artifact Files:
* [Forensics is fun.pptm](https://mercury.picoctf.net/static/52da699e0f203321c7c90ab56ea912d8/Forensics%20is%20fun.pptm)

### Approach
**1. Analisis _File_**  
Ini kita cuma dikasih _file_ PPT _random_ yang bila dibuka:  
![broken](images/MacroHard%20WeakEdge-1.JPG)  
Dari pengalaman yang sudah-sudah, file macam _doc_ sama _ppt_ itu sebenarnya semacam file **zip**. Yasudah kita ekstrak saja.

**2. Mencari File Mencurigakan**  
Setelah diekstrak, diperoleh hasil seperti berikut:  
![extracted pptm](images/MacroHard%20WeakEdge-2.JPG)  
Hmm sepertinya ada _file_ yang **SUS**.  
![sus file](images/MacroHard%20WeakEdge-3.JPG)  
Kan bener kan ada deretan karakter aneh. Dari namanya sudah mencurigakan. Ngapain _file_ ppt di dalamnya ada _file_ namanya **hidden**.
```
Z m x h Z z o g c G l j b 0 N U R n t E M W R f d V 9 r b j B 3 X 3 B w d H N f c l 9 6 M X A 1 f Q
```

**3. _Decode_ Kode dan Mendapatkan _Flag_**  
Sekarang tinggal menerjemahkan deretan karakter ini. Mengingat semuanya karakter alfanumerik dengan huruf besar dan kecil sedangkan kita tahu bahwa _flag_-nya semestinya mengandung karakter seperti ```{``` dan ```}```, maka deretan ini sepertinya hasil _encoding_ **Base64**. Tinggal kita _decode_ saja dan dapat _flag_-nya:  
![flag](images/MacroHard%20WeakEdge-4.JPG)  
Didapat _flag_-nya:
```
picoCTF{D1d_u_kn0w_ppts_r_z1p5}
```
### Reflections
Pengalaman menarik mengekstrak file **pptm** (karena _file_ ppt itu sebenarnya mirip seperti _file_ **ZIP** atau **RAR**), mencari file **SUS**, dan melakukan _decoding_ Base64.
  

---
[Back to home](../Readme.md)
