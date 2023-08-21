## Challenge Name: Intro to SysAdmin
>Category: Forensic

>Points: 449

>Solves: 18

### Challenge Description: 

Author: rorre

Welcome to the world of sysadmin! Our postgresql server was hacked, can you check out what's happening here?

Requirements:

* A linux system! VM or WSL (should) work too

Getting into the system:

1. Open your terminal
2.  Enter your root shell
3. Extract the tar file with ```tar -xf debian.tar.gz```
4. Set the root variable environment for convenience ```export DEBROOT=$PWD/debian```

    **WARNING**  
    Please **ENSURE** that the variable is **SET CORRECTLY**, or else **your system might be broken!** You can check this by running ```echo $DEBROOT``` and see if the variable has been indeed set.

5. Set up all the required Virtual Kernel FS
```
mount -v --bind /dev $DEBROOT/dev
mount -v --bind /dev/pts $DEBROOT/dev/pts
mount -vt proc proc $DEBROOT/proc
mount -vt sysfs sysfs $DEBROOT/sys
mount -vt tmpfs tmpfs $DEBROOT/run
```
6. Go inside the chroot
```
chroot "$DEBROOT" /usr/bin/env -i   \
    HOME=/root                      \
    TERM="$TERM"                    \
    PS1='(root chroot) \u:\w\$ '    \
    PATH=/usr/bin:/usr/sbin         \
    /bin/bash --login
```
7. If you see that you are root, now you are in the chroot environment. Happy hacking!

https://cdn.discordapp.com/attachments/1107668994477019218/1139898418823712781/debian.tar.gz


Artifact Files:
* [debian.tar.gz](https://cdn.discordapp.com/attachments/1107668994477019218/1139898418823712781/debian.tar.gz)

### Approach


cek log di /etc/log/postgresql

ternyata harus masuk

nyalain psql pake:
```service psql start```

gak bisa masuk

ke /etc/postgres ubah pg_hba.conf pake

cat -> pg_hba.conf

ubah method jadi trust

masuk pake
psql -U postgres

lihat database pake \lt

ke app pake \c app

lihat table pake \dt

select * from logs where message like 'COMPFEST*'; kek di log

dapat flag nya

**1. Access Virtual Kernel**

Untuk mengaksesnya tinggal ikuti saja langkah di deskripsi. Namun ingat kita perlu melakukannya dengan akses root. Untuk mengakses root shell masukkan command berikut:
```
sudo -i
```
Masukkan password root dan voila, root shell bisa diakses.
```
USER@HOST:XXX/CTF$ sudo -i
[sudo] password for USER: 
root@HOST:~# 
```
Sekarang, kita perlu pindah ke direktori berisi file ```debian.tar.gz```.
```
root@HOST: ~# cd PATH_TO_DEBIAN
```
Selanjutnya, tinggal ikuti petunjuk di deskripsi sampai prompt shell menjadi seperti ini:
```
root@HOST:PATH_TO_ROOT# chroot "$DEBROOT" /usr/bin/env -i   \
    HOME=/root                      \
    TERM="$TERM"                    \
    PS1='(root chroot) \u:\w\$ '    \
    PATH=/usr/bin:/usr/sbin         \
    /bin/bash --login
root@HOST:/# 
```
Jika sudah begini, maka sudah sukses masuk ke virtual kernel.

**2. Check Log**

Karena di deskripsi disebut bahwa server ```postgresql``` kena hack, kita perlu lihat log aktivitas nya dulu untuk lihat apa yang si hacker coba akses.

Setelah googling dan coba-coba dengan command berikut;
```
find / -name "postgresql"
```
Dapat beberapa direktori yang berhubungan dengan ```postgresql```:
```
/var/lib/postgresql
/var/cache/postgresql
/var/log/postgresql
/usr/lib/postgresql
/usr/share/doc/postgresql
/usr/share/postgresql
/etc/init.d/postgresql
/etc/postgresql
```
Terlihat ada direktori bernama ```/var/log/postgresql```. Ayo kita coba kesana dengan command ```cd``` lalu lihat isinya dengan ```ls```.
```
postgresql-15-main.log
```
Ada sebuah file log. Coba kita buka.
```
2023-08-12 11:55:10.800 UTC [11311] LOG:  starting PostgreSQL 15.3 (Debian 15.3-0+deb12u1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 12.2.0-14) 12.2.0, 64-bit
2023-08-12 11:55:10.801 UTC [11311] LOG:  listening on IPv6 address "::1", port 5432
2023-08-12 11:55:10.801 UTC [11311] LOG:  listening on IPv4 address "127.0.0.1", port 5432
2023-08-12 11:55:10.855 UTC [11311] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2023-08-12 11:55:10.978 UTC [11314] LOG:  database system was shut down at 2023-08-12 11:53:21 UTC
2023-08-12 11:55:11.040 UTC [11311] LOG:  database system is ready to accept connections
2023-08-12 11:55:14.552 UTC [11329] root@root FATAL:  role "root" does not exist
2023-08-12 11:55:27.234 UTC [11334] postgres@postgres ERROR:  syntax error at or near "DB" at character 8
2023-08-12 11:55:27.234 UTC [11334] postgres@postgres STATEMENT:  CREATE DB app;
2023-08-12 11:59:17.587 UTC [11334] postgres@postgres ERROR:  syntax error at or near "user" at character 14
2023-08-12 11:59:17.587 UTC [11334] postgres@postgres STATEMENT:  CREATE TABLE user 
	(
	    id	INT,
	    first_name	VARCHAR(512),
	    last_name	VARCHAR(512)
	);
2023-08-12 11:59:29.123 UTC [11334] postgres@postgres ERROR:  syntax error at or near "user" at character 14
2023-08-12 11:59:29.123 UTC [11334] postgres@postgres STATEMENT:  CREATE TABLE user (
	    id	INT,
	    first_name	VARCHAR(512),
	    last_name	VARCHAR(512)
	);
2023-08-12 11:59:39.314 UTC [11334] postgres@postgres ERROR:  syntax error at or near "CONNECT" at character 1
2023-08-12 11:59:39.314 UTC [11334] postgres@postgres STATEMENT:  CONNECT DATABASE app;
2023-08-12 11:59:46.387 UTC [11345] postgres@app ERROR:  syntax error at or near "user" at character 14
2023-08-12 11:59:46.387 UTC [11345] postgres@app STATEMENT:  CREATE TABLE user (
	    id	INT,
	    first_name	VARCHAR(512),
	    last_name	VARCHAR(512)
	);
2023-08-12 12:00:11.078 UTC [11312] LOG:  checkpoint starting: time
2023-08-12 12:00:27.395 UTC [11345] postgres@app ERROR:  syntax error at or near "user" at character 14
2023-08-12 12:00:27.395 UTC [11345] postgres@app STATEMENT:  CREATE TABLE user (
	    id	INT,
	    first_name	VARCHAR(512),
	    last_name	VARCHAR(512)
	);
2023-08-12 12:01:36.498 UTC [11345] postgres@app ERROR:  syntax error at or near "User" at character 14
2023-08-12 12:01:36.498 UTC [11345] postgres@app STATEMENT:  CREATE TABLE User 
	(
	    id	INT,
	    first_name	VARCHAR(512),
	    last_name	VARCHAR(512)
	);
2023-08-12 12:01:47.385 UTC [11312] LOG:  checkpoint complete: wrote 958 buffers (5.8%); 0 WAL file(s) added, 0 removed, 0 recycled; write=95.757 s, sync=0.306 s, total=96.308 s; sync files=259, longest=0.048 s, average=0.002 s; distance=4475 kB, estimate=4475 kB
2023-08-12 12:01:54.629 UTC [11345] postgres@app ERROR:  syntax error at or near "USER" at character 14
2023-08-12 12:01:54.629 UTC [11345] postgres@app STATEMENT:  CREATE TABLE USER 
	(
	    id	INT,
	    first_name	VARCHAR(512),
	    last_name	VARCHAR(512)
	);
2023-08-12 12:02:30.745 UTC [11345] postgres@app ERROR:  syntax error at or near "USER" at character 14
2023-08-12 12:02:30.745 UTC [11345] postgres@app STATEMENT:  CREATE TABLE USER 
	(
	    "id"	INT,
	    "first_name"	VARCHAR(512),
	    "last_name"	VARCHAR(512)
	);
2023-08-12 12:03:07.235 UTC [11345] postgres@app ERROR:  syntax error at or near "USER" at character 14
2023-08-12 12:03:07.235 UTC [11345] postgres@app STATEMENT:  CREATE TABLE USER(
	    "id"		INT,
	    "first_name"	VARCHAR(512),
	    "last_name"		VARCHAR(512)
	);
2023-08-12 12:05:11.472 UTC [11312] LOG:  checkpoint starting: time
2023-08-12 12:05:15.191 UTC [11312] LOG:  checkpoint complete: wrote 34 buffers (0.2%); 0 WAL file(s) added, 0 removed, 0 recycled; write=3.359 s, sync=0.110 s, total=3.719 s; sync files=28, longest=0.068 s, average=0.004 s; distance=151 kB, estimate=4042 kB
2023-08-12 12:08:43.908 UTC [11345] postgres@app ERROR:  column "COMPFEST*" does not exist at character 39
2023-08-12 12:08:43.908 UTC [11345] postgres@app STATEMENT:  SELECT * FROM LOGS WHERE message LIKE "COMPFEST*";
2023-08-12 12:10:11.291 UTC [11312] LOG:  checkpoint starting: time
2023-08-12 12:10:18.009 UTC [11312] LOG:  checkpoint complete: wrote 63 buffers (0.4%); 0 WAL file(s) added, 0 removed, 0 recycled; write=6.265 s, sync=0.221 s, total=6.718 s; sync files=27, longest=0.057 s, average=0.009 s; distance=337 kB, estimate=3672 kB
2023-08-12 12:11:35.063 UTC [11311] LOG:  received smart shutdown request
2023-08-12 12:11:35.542 UTC [11311] LOG:  background worker "logical replication launcher" (PID 11317) exited with exit code 1
2023-08-12 12:11:35.542 UTC [11312] LOG:  shutting down
2023-08-12 12:11:35.715 UTC [11312] LOG:  checkpoint starting: shutdown immediate
2023-08-12 12:11:36.420 UTC [11312] LOG:  checkpoint complete: wrote 0 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.001 s, sync=0.001 s, total=0.879 s; sync files=0, longest=0.000 s, average=0.000 s; distance=0 kB, estimate=3305 kB
2023-08-12 12:11:36.425 UTC [11311] LOG:  database system is shut down
root@anugrahfawwaz-ZenBook-UX425EA-2nd25EA:/var/log/postgresql# find / -name "log"
/var/log
/dev/log
root@anugrahfawwaz-ZenBook-UX425EA-2nd25EA:/var/log/postgresql# find / -name "postgresql"
/var/lib/postgresql
/var/cache/postgresql
/var/log/postgresql
/usr/lib/postgresql
/usr/share/doc/postgresql
/usr/share/postgresql
/etc/init.d/postgresql
/etc/postgresql
root@anugrahfawwaz-ZenBook-UX425EA-2nd25EA:/var/log/postgresql# ls
postgresql-15-main.log
root@anugrahfawwaz-ZenBook-UX425EA-2nd25EA:/var/log/postgresql# cat postgresql-15-main.log 
2023-08-12 11:55:10.800 UTC [11311] LOG:  starting PostgreSQL 15.3 (Debian 15.3-0+deb12u1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 12.2.0-14) 12.2.0, 64-bit
2023-08-12 11:55:10.801 UTC [11311] LOG:  listening on IPv6 address "::1", port 5432
2023-08-12 11:55:10.801 UTC [11311] LOG:  listening on IPv4 address "127.0.0.1", port 5432
2023-08-12 11:55:10.855 UTC [11311] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2023-08-12 11:55:10.978 UTC [11314] LOG:  database system was shut down at 2023-08-12 11:53:21 UTC
2023-08-12 11:55:11.040 UTC [11311] LOG:  database system is ready to accept connections
2023-08-12 11:55:14.552 UTC [11329] root@root FATAL:  role "root" does not exist
2023-08-12 11:55:27.234 UTC [11334] postgres@postgres ERROR:  syntax error at or near "DB" at character 8
2023-08-12 11:55:27.234 UTC [11334] postgres@postgres STATEMENT:  CREATE DB app;
2023-08-12 11:59:17.587 UTC [11334] postgres@postgres ERROR:  syntax error at or near "user" at character 14
2023-08-12 11:59:17.587 UTC [11334] postgres@postgres STATEMENT:  CREATE TABLE user 
	(
	    id	INT,
	    first_name	VARCHAR(512),
	    last_name	VARCHAR(512)
	);
2023-08-12 11:59:29.123 UTC [11334] postgres@postgres ERROR:  syntax error at or near "user" at character 14
.....
2023-08-12 12:08:43.908 UTC [11345] postgres@app ERROR:  column "COMPFEST*" does not exist at character 39
2023-08-12 12:08:43.908 UTC [11345] postgres@app STATEMENT:  SELECT * FROM LOGS WHERE message LIKE "COMPFEST*";
2023-08-12 12:10:11.291 UTC [11312] LOG:  checkpoint starting: time
2023-08-12 12:10:18.009 UTC [11312] LOG:  checkpoint complete: wrote 63 buffers (0.4%); 0 WAL file(s) added, 0 removed, 0 recycled; write=6.265 s, sync=0.221 s, total=6.718 s; sync files=27, longest=0.057 s, average=0.009 s; distance=337 kB, estimate=3672 kB
2023-08-12 12:11:35.063 UTC [11311] LOG:  received smart shutdown request
2023-08-12 12:11:35.542 UTC [11311] LOG:  background worker "logical replication launcher" (PID 11317) exited with exit code 1
.....
2023-08-12 12:11:36.420 UTC [11312] LOG:  checkpoint complete: wrote 0 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.001 s, sync=0.001 s, total=0.879 s; sync files=0, longest=0.000 s, average=0.000 s; distance=0 kB, estimate=3305 kB
2023-08-12 12:11:36.425 UTC [11311] LOG:  database system is shut down

```
Terlihat hacker mencoba mengakses tabel ```user``` berkali-kali tapi kena synthax error mulu (press F buat hacker). Namun yang menarik adalah di bagian ini:
```
2023-08-12 12:08:43.908 UTC [11345] postgres@app ERROR:  column "COMPFEST*" does not exist at character 39
2023-08-12 12:08:43.908 UTC [11345] postgres@app STATEMENT:  SELECT * FROM LOGS WHERE message LIKE "COMPFEST*";
```
Jadi ada tabel namanya ```LOGS``` yang berisi kolom ```message``` dan salah satu message nya sepertinya mengandung kata ```COMPFEST```. Menarik, ini bukannya format flag ya? sepertinya _flag_-nya ada di database ```app``` (terlihat dari bagian ```postgres@app``` dimana ```postgres``` adalah nama user dan ```app``` adalah nama database) pada tabel ```LOGS``` di kolom ```message```.

**3. Access the Database**

sekarang kita coba akses database menggunakan command:
```
psql
```
Didapat:
```
psql: error: connection to server on socket "/var/run/postgresql/.s.PGSQL.5432" failed: No such file or directory
	Is the server running locally and accepting connections on that socket?
```
Lah kok error? Apa database nya dimatiin keknya?

Setelah ku cari di internet ku nemu [website ini](https://tableplus.com/blog/2018/10/how-to-start-stop-restart-postgresql-server.html) yang menjelaskan bagaimana cara menyalakan dan mematikan postgresql di berbagai OS. Untuk linux, kita gunakan command berikut:
```
service postgresql start
```
Karena kita sudah login sebagai root, tidak perlu sudo lagi.

Sekarang coba kita jalankan.
```
Starting PostgreSQL 15 database server: main
```
Tekan enter
```
Starting PostgreSQL 15 database server: main
.
```
Harusnya sekarang sudah nyala. Coba kita masukkan command ```psql```:
```
psql: error: connection to server on socket "/var/run/postgresql/.s.PGSQL.5432" failed: FATAL:  role "root" does not exist
```
Nah error nya dah beda berarti seenggaknya _server_-nya sudah nyala.

Sekarang pertanyaanya gimana cara masuknya?

Hmm baru inget, defaultnya user postgresql kan ```postgres```, coba kita masuk sebagai ```postgres```:
```
psql -U postgres
```
Didapat:
```
psql: error: connection to server on socket "/var/run/postgresql/.s.PGSQL.5432" failed: FATAL:  Peer authentication failed for user "postgres"
```
Lah gagal? Coba kita ganti user ke postgres.
```
sudo -i postgres
```
Hasil:
```
bash: sudo: command not found
```
Lah gak bisa ganti user dong. Hmm..harus pake cara apa ya?

Setelah ku cari di internet, ternyata ada file konfigurasi akses postgresql namanya [pg_hba.conf](https://www.postgresql.org/docs/current/auth-pg-hba-conf.html) yang berisi konfigurasi untuk akses postgresql baik local atau remote. Nah ada bagian menarik namanya ```method```. Bagian ini berguna untuk memeriksa bagaimana metode autentikasi user yang mencoba mengakses usernema tertentu lewat local/remote. Kalau kita utak-atik ini, kita bisa dapat akses masuk ke postgresql.

Untuk tahu apa method yang dipake user postgres, kita cari dulu filenya:
```
find / -name "pg_hba.conf"
```
didapat:
```
/etc/postgresql/15/main/pg_hba.conf
```
Kita langsung saja open manggunakan ```cat```:
```
cat /etc/postgresql/15/main/pg_hba.conf
```
Diperoleh:
```
# PostgreSQL Client Authentication Configuration File
# ===================================================
#
# Refer to the "Client Authentication" section in the PostgreSQL
# documentation for a complete description of this file.  A short
# synopsis follows.
#
# This file controls: which hosts are allowed to connect, how clients
# are authenticated, which PostgreSQL user names they can
.....
# DO NOT DISABLE!
# If you change this first entry you will need to make sure that the
# database superuser can access the database using some other method.
# Noninteractive access to all databases is required during automatic
# maintenance (custom daily cronjobs, replication, and similar tasks).
#
# Database administrative login by Unix domain socket
local   all             postgres                                peer

# TYPE  DATABASE        USER            ADDRESS                 METHOD

# "local" is for Unix domain socket connections only
local   all             all                                     peer
# IPv4 local connections:
host    all             all             127.0.0.1/32            scram-sha-256
# IPv6 local connections:
host    all             all             ::1/128                 scram-sha-256
# Allow replication connections from localhost, by a user with the
# replication privilege.
local   replication     all                                     peer
host    replication     all             127.0.0.1/32            scram-sha-256
host    replication     all             ::1/128                 scram-sha-256
```
Terlihat di bagian bawah ada list koneksi, user, dan methos. Selain itu, terlihat bahwa ```postgres``` menggunakan autentikasi method, yakni memeriksa apakah user system sama dengan ```postgres```.

Jika kita lihat di [dokumentasi](https://www.postgresql.org/docs/current/auth-pg-hba-conf.html), ternyata ada ```auth-method``` bernama ```trust``` yang mana kita bisa akses basis data sebagai user apa pun tanpa autentikasi/password. Sepertinya hal ini menarik untuk bypass autentikasi postgresql.

Mari kita edit _file_-nya! (Spoiler alert: tidak sesuai perkiraan)
```
nano /etc/postgresql/15/main/pg_hba.conf
```
Daan...
```
bash: nano: command not found
```
Binary ```nano``` nya gak ada dong saudara/i. Hmm pake apa ya? coba ```vi```/```vim```:
```
vi nano /etc/postgresql/15/main/pg_hba.conf
```
Hasil:
```
bash: vi: command not found
```
Coba kalau ```vim```:
```
vim nano /etc/postgresql/15/main/pg_hba.conf
```
Hasil:
```
bash: vim: command not found
```
Hmm..kudu pake command apa ya?

Setelah searching di internet, baru tahu ternyata command ```cat``` bisa buat edit file. Formatnya berikut:
```
cat -> PATH_TO_FILE
```
Namun ini sistemnya ```write``` aja jadi semua isi _file_-nya bakal keganti. Berarti kita edit dulu konfigurasinya:
```
# PostgreSQL Client Authentication Configuration File
# ===================================================
#
# Refer to the "Client Authentication" section in the PostgreSQL
# documentation for a complete description of this file.  A short
# synopsis follows.
#
# This file controls: which hosts are allowed to connect, how clients
# are authenticated, which PostgreSQL user names they can
.....
# DO NOT DISABLE!
# If you change this first entry you will need to make sure that the
# database superuser can access the database using some other method.
# Noninteractive access to all databases is required during automatic
# maintenance (custom daily cronjobs, replication, and similar tasks).
#
# Database administrative login by Unix domain socket
local   all             postgres                                trust

# TYPE  DATABASE        USER            ADDRESS                 METHOD

# "local" is for Unix domain socket connections only
local   all             all                                     peer
# IPv4 local connections:
host    all             all             127.0.0.1/32            scram-sha-256
# IPv6 local connections:
host    all             all             ::1/128                 scram-sha-256
# Allow replication connections from localhost, by a user with the
# replication privilege.
local   replication     all                                     peer
host    replication     all             127.0.0.1/32            scram-sha-256
host    replication     all             ::1/128                 scram-sha-256
```
Sekarang mari kita edit:
```
root@HOST:/var/log/postgresql# cat  -> /etc/postgresql/15/main/pg_hba.conf
.....
# DO NOT DISABLE!
# If you change this first entry you will need to make sure that the
# database superuser can access the database using some other method.
# Noninteractive access to all databases is required during automatic
# maintenance (custom daily cronjobs, replication, and similar tasks).
#
# Database administrative login by Unix domain socket
local   all             postgres                                trust

# TYPE  DATABASE        USER            ADDRESS                 METHOD

# "local" is for Unix domain socket connections only
local   all             all                                     peer
# IPv4 local connections:
host    all             all             127.0.0.1/32            scram-sha-256
# IPv6 local connections:
host    all             all             ::1/128                 scram-sha-256
# Allow replication connections from localhost, by a user with the
# replication privilege.
local   replication     all                                     peer
host    replication     all             127.0.0.1/32            scram-sha-256
host    replication     all             ::1/128                 scram-sha-256
^C
root@HOST:/var/log/postgresql#
```
Jangan lupa tekan ```ctrl+c``` untuk mengakhiri edit.

Sekarang kita coba login lagi:
```
psql -U postgres
```
Hasil:
```
psql: error: connection to server on socket "/var/run/postgresql/.s.PGSQL.5432" failed: FATAL:  Peer authentication failed for user "postgres"
```
Weit gagal? Tunggu...itu kenapa bilang autentikasinya masih ```peer```? oh iya bener, belum kita restart service _postgresql_-nya. Untuk me-_restart_ gunakan command berikut untuk mematikan service:
```
service postgresql stop
```
Hasil:
```
Stopping PostgreSQL 15 database server: main.
```
Sekarang kita coba jalankan kembali:
```
service postgresql start
```
Hasil:
```
Starting PostgreSQL 15 database server: main
.
```
Sekarang coba kita akses ulang:
```
psql -U postgres
```
Hasil:
```
root@HOST:/var/log/postgresql# psql -U postgres
psql (15.3 (Debian 15.3-0+deb12u1))
Type "help" for help.

postgres=# 
```
Alhamdulillah tembus. 

**4. Get the Flag**

Terakhir, tinggal mendapatkan flag. Dari hint kita tahu bahwa flag ada di tabel ```logs``` pada database ``app``. Pertama kita coba akses database ```app``` menggunakan command:
```
\c app
```
Hasil:
```
You are now connected to database "app" as user "postgres".
app=# 
```
Seakarang tinggal melakukan query yang mirip dengan si hacker untuk mendapatkan mesage yang diawali ```COMPFEST```:
```
SELECT * FROM logs WHERE message LIKE 'COMPFEST%';
```
Hasil:
```
 id  |              message               
-----+------------------------------------
 229 | COMPFEST15{M4st3R_0f_l0g_ch3ck1Ng}
(1 row)
```
Alhamdulillah dapat _flag_-nya!
```
COMPFEST15{M4st3R_0f_l0g_ch3ck1Ng}
```

### Reflections

Permulaan yang lumayan membingungkan untuk menjadi SysAdmin, tapi akhirnya ketemu lah. Disini jadi belajar baca log database serta ngubah config database. Selain itu, nemu trick command di shell linux baru kayak makai ```cat``` buat ngubah file. Tapi jujur, rather than becoming SysAdmin, ini challenge _feel_-nya kok kek kita yang jadi hacker ya.

---
[Back to home](../Readme.md)
