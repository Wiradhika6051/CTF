## Challenge Name: Static ain't always noise
>Category: General

>Points: 20

>Solves: 55k+

### Challenge Description: 

Can you look at the data in this binary: [static](https://mercury.picoctf.net/static/7495259e963bd5b67d0fb8b616652618/static)? This [BASH script](https://mercury.picoctf.net/static/7495259e963bd5b67d0fb8b616652618/ltdis.sh) might help!

Artifact Files:
* [static](https://mercury.picoctf.net/static/7495259e963bd5b67d0fb8b616652618/static)
* [ltdis.sh](https://mercury.picoctf.net/static/7495259e963bd5b67d0fb8b616652618/ltdis.sh)

### Approach

**1. Analisa File**

Karena aku mengerjakan challenge ini di laptop Windows tanpa WSL, maka step-step ini aku lakukan via webshell.

Pertama kita download file ```static``` dengan command:
```
wget https://mercury.picoctf.net/static/7495259e963bd5b67d0fb8b616652618/static
```
Lalu untuk BASH script:
```
wget https://mercury.picoctf.net/static/7495259e963bd5b67d0fb8b616652618/ltdis.sh
```
Coba kita lihat apa jenis file ```static```
```
file static
```
Hasil:
```
static: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=bedc412be2156b04706c1f2568fcff42306dea27, not stripped
```
Ternyata ini file executable untuk linux 64-bit.

Sekarang coba kita bukan BASH script:
```
cat ltdis.sh
```
Hasil:
```
#!/bin/bash



echo "Attempting disassembly of $1 ..."


#This usage of "objdump" disassembles all (-D) of the first file given by 
#invoker, but only prints out the ".text" section (-j .text) (only section
#that matters in almost any compiled program...

objdump -Dj .text $1 > $1.ltdis.x86_64.txt


#Check that $1.ltdis.x86_64.txt is non-empty
#Continue if it is, otherwise print error and eject

if [ -s "$1.ltdis.x86_64.txt" ]
then
        echo "Disassembly successful! Available at: $1.ltdis.x86_64.txt"

        echo "Ripping strings from binary with file offsets..."
        strings -a -t x $1 > $1.ltdis.strings.txt
        echo "Any strings found in $1 have been written to $1.ltdis.strings.txt with file offset"



else
        echo "Disassembly failed!"
        echo "Usage: ltdis.sh <program-file>"
        echo "Bye!"
fi
```
Sepertinya ini adalah bash script untuk disassemble binary dan menyimpan string nya ke suatu file.

**2. How to get the flag?**
Karena kita punya executable dan BASH script untuk decompile executable dan menyimpan string yang ada di executable ke file, sepertinya kita tinggal menjalankan script ini saja. Dan karena flagnya pasti string (harusnya), flagnya kemungkinan ada di dalam file hasil ekstraksi string.

Dari isi bash scriptnya, cara menggunakannya adalah:
```
ltdis.sh <program-file>
```
Berarti tinggal kita jalankan command berikut:
```
./ltdis.sh static
```
Dan program pun berjalan:
```
Attempting disassembly of static ...
Disassembly successful! Available at: static.ltdis.x86_64.txt
Ripping strings from binary with file offsets...
Any strings found in static have been written to static.ltdis.strings.txt with file offset
```
Lalu kita lihat isi direktorinya:
```
ls
```
Didapat:
```
README.txt  enc       static                    static.ltdis.x86_64.txt  warm
cat.jpg     ltdis.sh  static.ltdis.strings.txt  transformation.py
```
Terlihat ada dua file baru hasil output script tadi yakni ```static.ltdis.strings.txt``` dan ```static.ltdis.x86_64.txt```. Karena flagnya berupa string, jadi kemungkinan ada di file ```static.ltdis.strings.txt```. Mari kita buka dengan command berikut:
```
cat static.ltdis.strings.txt
```
Dan didapat:
```
    238 /lib64/ld-linux-x86-64.so.2
    361 libc.so.6
    36b puts
    370 __cxa_finalize
    37f __libc_start_main
    391 GLIBC_2.2.5
    39d _ITM_deregisterTMCloneTable
    3b9 __gmon_start__
    3c8 _ITM_registerTMCloneTable
    660 AWAVI
    667 AUATL
    6ba []A\A]A^A_
    6e8 Oh hai! Wait what? A flag? Yes, it's around here somewhere!
    7c7 ;*3$"
   1020 picoCTF{d15a5m_t34s3r_f6c48608}
   1040 GCC: (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.0
   1671 crtstuff.c
   167c deregister_tm_clones
   1691 __do_global_dtors_aux
   16a7 completed.7698
   16b6 __do_global_dtors_aux_fini_array_entry
   16dd frame_dummy
   16e9 __frame_dummy_init_array_entry
   1708 static.c
   1711 __FRAME_END__
   171f __init_array_end
   1730 _DYNAMIC
   1739 __init_array_start
   174c __GNU_EH_FRAME_HDR
   175f _GLOBAL_OFFSET_TABLE_
   1775 __libc_csu_fini
   1785 _ITM_deregisterTMCloneTable
   17a1 puts@@GLIBC_2.2.5
   17b3 _edata
   17ba __libc_start_main@@GLIBC_2.2.5
   17d9 __data_start
   17e6 __gmon_start__
   17f5 __dso_handle
   1802 _IO_stdin_used
   1811 __libc_csu_init
   1821 __bss_start
   182d main
   1832 __TMC_END__
   183e _ITM_registerTMCloneTable
   1858 flag
   185d __cxa_finalize@@GLIBC_2.2.5
   187a .symtab
   1882 .strtab
   188a .shstrtab
   1894 .interp
   189c .note.ABI-tag
   18aa .note.gnu.build-id
   18bd .gnu.hash
   18c7 .dynsym
   18cf .dynstr
   18d7 .gnu.version
   18e4 .gnu.version_r
   18f3 .rela.dyn
   18fd .rela.plt
   1907 .init
   190d .plt.got
   1916 .text
   191c .fini
   1922 .rodata
   192a .eh_frame_hdr
   1938 .eh_frame
   1942 .init_array
   194e .fini_array
   195a .dynamic
   1963 .data
   1969 .bss
   196e .comment
```
Pada line 1020 terdapat flag untuk challenge ini. Flag nya adalah:
```
picoCTF{d15a5m_t34s3r_f6c48608}
```

### Reflections
Permulaan bagus untuk belajar tentang bashscript dan teaser untuk konsep disassembly seperti nama flagnya.
  

---
[Back to home](../Readme.md)
