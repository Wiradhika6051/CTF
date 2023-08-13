## Challenge Name: Rivest Shamir Adleman
>Category: Cryptography

>Points: 464

>Solves: 15

### Challenge Description: 

For the sake of maintaing security, the IT Dev team of Collective Inc. regularly changes their encryption system every sixth months. This time, they have made three new RSA-based encryption system and you are the one in charge testing them. They ask you to test these three algorithms by finding their vulnerabilities if possible with different test cases each round. Feeling intrigued, you accept their request filled with determination.

```nc 34.101.174.85 10004```

Original Author: potsu

Artifact Files:
* [chall.py](https://ctf.compfest.id/files/bad87d139d2137cf8a8fd6c243342125/chall.py?token=eyJ1c2VyX2lkIjoxMCwidGVhbV9pZCI6bnVsbCwiZmlsZV9pZCI6MTl9.ZNTSbQ.hgcGOPcif61G7YipMlwlsIPJ33A)

### Approach

**1. Analyze the file**

Berikut adalah isi file ```chall.py``` :
```
from Crypto.Util.number import GCD, getPrime, bytes_to_long
from sympy import nextprime
from random import choice
from secret import FLAG
import os

def modeA():
    n = getPrime(512)
    return n

def modeB():
    e = 3
    return e

def modeC(e):
    while True:
        p = getPrime(512)
        q = nextprime(nextprime(nextprime(p)))
        if GCD(e, (p-1)*(q-1)) == 1:
            break
    n = p*q
    return n

def setup():
    p = getPrime(512)
    q = getPrime(512)
    e = 65537
    return p, q, e

def main():
    print('Starting session.')
    flag = FLAG
    stages = 20
    modes = ['A', 'B', 'C']
    for i in range(stages):
        p, q, e = setup()
        n = p*q
        m = bytes_to_long(os.urandom(32))
        mode = choice(modes)
        if mode == 'A':
            n = modeA()
        elif mode == 'B':
            e = modeB()
        elif mode == 'C':
            n = modeC(e)
        else:
            raise AssertionError('Unknown Mode')

        c = pow(m, e, n)
        print(f'mode = {mode}')
        print(f'n = {n}')
        print(f'e = {e}')
        print(f'c = {c}')

        inp = input("Your answer: ")
        if not inp.isnumeric():
            raise AssertionError('Input is not integer.')
        
        if int(inp) == m:
            print('Correct!')
        else:
            print('Wrong answer!')
            break

    if i == (stages - 1):
        print(f'Congrats! Here\'s your flag: {flag}')
    else:
        print(f'Sorry you have failed at round {i + 1}')
    print('Ending session.')

if __name__ == '__main__':
    try:
        main()
    except:
        print('An error has occured.')
```
Penjelasan tentang kode soal adalah sebagai berikut:
```
def main():
    print('Starting session.')
    flag = FLAG
    stages = 20
    modes = ['A', 'B', 'C']
    for i in range(stages):
        p, q, e = setup()
        n = p*q
        m = bytes_to_long(os.urandom(32))
        mode = choice(modes)
        if mode == 'A':
            n = modeA()
        elif mode == 'B':
            e = modeB()
        elif mode == 'C':
            n = modeC(e)
        else:
            raise AssertionError('Unknown Mode')

        c = pow(m, e, n)
        print(f'mode = {mode}')
        print(f'n = {n}')
        print(f'e = {e}')
        print(f'c = {c}')

        inp = input("Your answer: ")
        if not inp.isnumeric():
            raise AssertionError('Input is not integer.')
        
        if int(inp) == m:
            print('Correct!')
        else:
            print('Wrong answer!')
            break

    if i == (stages - 1):
        print(f'Congrats! Here\'s your flag: {flag}')
    else:
        print(f'Sorry you have failed at round {i + 1}')
    print('Ending session.')

if __name__ == '__main__':
    try:
        main()
    except:
        print('An error has occured.')
```
Bagian ini merupakan bagian utama program. Program pertama akan membaca ```FLAG``` dari file python di local server, lalu melakukan looping sebanyak ```stages```, dalam hal ini adalah **20**. Di tiap stage, akan dilakukan pemilihan mode di stage tersebut secara acak, apakah **A**, **B**, atau **C**. Terlepas dari mode yang dipilih, akan dilakukan inisialisasi awal nilai ```p```,```q```, dan ```e``` melalui fungsi ```setup()```, serta inisialisasi nilai ```n``` dan ```m```. Kemudian, dilakukan inisialisasi lanjutan berdasarkan mode-nya. Jika modenya adalah **A**, nilai ```n``` akan diperbaharui dengan nilai keluaran fungsi ```modeA()```. Jika modenya adalah **B**, nilai ```e``` akan diperbaharui dengan nilai keluaran fungsi ```modeB()```. Terkahir, jika modenya adalah **C**, nilai ```n``` akan diperbaharui dengan nilai keluaran fungsi ```modeC(e)```.

Setelah proses inisialisasi selesai, dilakukan proses perhitungan untuk mendapatkan ciphertext (```c```). Selanjutnya, nilai ```mode```, ```n```, ```e```, dan ```c``` akan ditampilkan ke pengguna.

Langkah selanjutnya, program akan menerima input plaintext (```m```) yang di-_generate_ di stage ini. Jika tebakan benar, maka akan lanjut ke stage berikutnya. Jika gagal, maka akan keluar dari loop.

Jika pengguna bisa menyelesaikan semua stage, maka flag akan ditampilkan ke layar.

Berikut adalah isi dari fungsi ```setup()```:
```
def setup():
    p = getPrime(512)
    q = getPrime(512)
    e = 65537
    return p, q, e
```
Fungsi ini akan menghasilkan nilai ```p``` dan ```q```, yang merupakan bilangan prima sepanjang 512 bit / 64 bytes.  Selain itu, akan dikembalikan juga nilai ```e``` yakni konstanta dengan nilai **65537**.

Selanjutnya adalah fungsi ```modeA()```:
```
def modeA():
    n = getPrime(512)
    return n
```
Fungsi ini akan mengembalikan nilai ```n``` berupa bilangan prima 512-bit. Sebenarnya dari sini, terlihat bahwa ```modeA()``` memiliki exploit, yakni ```n``` merupakan bilangan prima. Cara exploit nya akan dijelaskan di bagian pembuatan ```script```.

Selanjutnya adalah fungsi ```modeB()```:
```
def modeB():
    e = 3
    return e
```
Fungsi ini akan mengembalikan nilai ```e``` dengan nilai konstan yakni **3**. Dari sini bisa terlihat bahwa ```modeB()``` rentang dengan serangan yang memanfaatkan fakta bahwa eksponen publik (```e```) kecil.

Terakhir adalah fungsi ```modeC()```:
```
def modeC(e):
    while True:
        p = getPrime(512)
        q = nextprime(nextprime(nextprime(p)))
        if GCD(e, (p-1)*(q-1)) == 1:
            break
    n = p*q
    return n
```
Fungsi ini akan meng-_generate_ nilai ```n``` dengan terlebih dahulu meng-_generate_ nilai ```p``` dan ```q```. Jika kita perhatikan ada fakta menarik,yakni ```q``` merupakan bilangan prima ketiga setelah ```p```. Karena ```p``` cukup besar (512-bit), jarak ```p``` dan ```q``` tidak terlalu jauh relatif ke ```n``` dimana persamaan berikut akan terpenuhi:
```
|p-q| < n ^ (1/4)
```
Hal ini bisa menjadi exploit untuk mendapatkan ```p``` dan ```q```.

**2. Craft Payload and Get the Flag**

Untuk langkah selanjutnya, kita akan membuat script untuk mendapatkan flag. Kita bahas untuk setiap mode:

1. Mode A. Pada mode ini kita akan mengeksploitasi vulnerability yakni ```n``` merupakan bilangan prima. Kode untuk menyelesaikannya adalah sebagai berikut:
```
#vulnerability p = prime
def solve_A(N,c):
  e = 65537
  phi_p = N-1
  d = inverse(e,phi_p)
  m = pow(c,d,N)
  print("Plaintext (m): ",m)
  return m
```
Karena kita tahu ```n``` adalah prima, maka faktornya hanyalah ```p``` saja. Karena faktornya cuma p, nilai ```phi_n``` akan menjadi:
```
phi_n = p-1...(1)
```
karena ```n```==```p```, maka persamaan akan menjadi:
```
phi_n = phi_p = n-1...(2)
```
Jika kita sudah mendapat ```phi_n```, kita bisa mendapatkan kunci privat (```d```) dengan persamaan:
```
d = 1+ k* (phi_p)/ e ...(3)
```
Atau kita bisa tinggal menggunakan fungsi ```inverse()``` bawaan library ```Crypto```. 

Jika ```d```, sudah didapatkan, tinggal pangkatkan ```ciphertext``` dengan ```d```, lalu hasilnya dimodulo dengan ```n``` (persamaan dekripsi RSA) dan didapatkan plaintext-nya.

Side info: fungsi ```pow()``` bisa menerima argumen ke 3, yakni nilai modulo sehingga pemanggilan berikut:
```
pow(a,b,c)
```
sama dengan
```
(a ** b) % c
```

2. Mode B. Pada mode ini kita akan mengeksploitasi vulnerability yakni ```e``` nya sangat kecil (e <<< N) sehingga pada sebagian besar kasus, p ** e akan lebih kecil dari N dan efek modulo tidak akan terasa. Kode untuk menyelesaikannya adalah sebagai berikut:
```
#vulnerability e kecil (e=3)
def solve_B(c):
  m = cbrt(c)
  print("Plaintext (m): ",m)
  return m
```
```cbrt()``` adalah fungsi bawaan library ```sympy``` untuk menghitung akar pangkat 3 yang lebih efisien dalam hal waktu ibandingkan menggunakan ```pow()```. Alasan kita mencari akar pangkat 3 adalah dari data yang kita tahu, pada sebagian besar kasus:
```
p ** e < n
```
Sehingga persamaan enkripsinya akan menjadi berikut:
```
c = p **e ...(4)
```
Dalam kasus ini untuk mendapatkan plaintext, persamaannya adalah:
```
p = c ** (1/e) ...(5)
```
Karena ```e``` = 3, maka persamaannya akan menjadi:
```
p = c ** (1/3) ...(6)
```
Atau dengan kata lain adalah plaintext adalah akar pangkat 3 dan ciphertext.

3. Mode C. Pada mode ini kita akan mengeksploitasi vulnerability yakni nilai ```p``` dan ```q``` yang cukup berdekatan, yakni memenuhi persamaan:
```
|p-q| < n ^ (1/4)...(7)
```
Kita bisa melakukan eksploit dengan menggunakan **fermat attack**. Kode untuk melakukan serangannya adalah sebagai berikut:
```
#fermat attack (p dan q deketan, |p-1|<N^1/4)
def solve_C(N,c):
  e = 65537
  #cari p dan q dengane near consecutive prime exploit menggunakan fermat attack (|p-q| < N ^ 1/4)
  a,_ = gmpy2.iroot(N,2)
  while a*a - N <0:
    a +=1
  b = int(a*a - N)
  sqrt_b,_ = gmpy2.iroot(b,2)
  p = int(a - sqrt_b)
  q = N//p
  phi_p = (p-1) * (q-1)
  d = inverse(e,phi_p)
  m = pow(c,d,N)
  print("Plaintext (m): ",m)
  return m
```
Cara melakukannya adalah sebagai berikut:
1. Kita melakukan aproksimasi untuk mendapatkan ```p``` dengan mencari akar pangkat 2 dari ```n```.
2. Kemudian kita hitung nilai:
```
a*a-n
```
Jika nilainya kurang dari 0, inkremen ```a```. (Sebenarnya setelah kubaca-baca lagi, di bagian ```while``` harusnya ada pengecekan apakah ```a*a-n``` itu _perfect square_ (hasil pangkat dua bilangan, misalnya 16 itu _perfect square_ karena merupakan hasil dari 4 **2), tapi kebetulan di server tembus jadi yaudah wkwkw).

3. Jika sudah didapat nilai **a** yang memenuhi, hitung ```a*a-n``` lalu dikonversi ke integer dan hasilnya di-_assign_ ke variabel ```b```.

4. Selanjutnya, karena diasumsikan ```b``` itu _perfect square_, maka cari nilai akar dari ```b``` lalu assign ke variabel bernama ```sqrt_b```. Fungsi ```gmpy.iroot(b,2)``` berguna untuk mencari akar pangkat 2 dari b dengan lebih efisien. Fungsi ini bawaan library **gmpy**.

5. Nilai ```p``` bisa didapatkan dengan mengurangi **a** dengan **sqrt_b**, lalu hasilnya dijadikan integer.

6. Nilai ```q``` bisa didapatkan dengan membagi ```n``` dengan ```p```, lalu hasilnya dijadikan integer. (Operator **//** itu operator pembagian di python yang hasilnya tetap integer meski pembagiannya bersisa).

7. Karena ```p``` dan ```q``` sudah didapay, tinggal mendapatkan ```phi_n``` dengan rumus: (note: di kode typo malah jadi ```phi_p``` tapi ku dah mager ngubahnya)
```
phi_n = (p-1) * (q-1)...(8)
```

8. Jika ```phi_n``` sudah didapat, mendapatkan ```d``` tinggal melakukan inverse modulo antara ```e``` dengan ```phi_n```. Lalu setelah ```d``` didapat, tinggal lakukan proses dekripsi RSA biasa dan didapat _plaintext_-nya.

Dengan memanfaatkan exploit yang ada, berikut adalah kode untuk mendapatkan flag: (Note: semestinya ini dites di lokal dulu, namun ```pwntools``` rada ngebug kalau konek ke proses lokal di windows, jadi pas itu ku langsung nembak ke server dan kebetulan dapet Alhamdulillah)L\:
```
from Crypto.Util.number import inverse
from sympy import cbrt,nextprime
import gmpy2
import pwn

#vulnerability p = prime
def solve_A(N,c):
  e = 65537
  phi_p = N-1
  d = inverse(e,phi_p)
  m = pow(c,d,N)
  print("Plaintext (m): ",m)
  return m

#vulnerability e kecil (e=3)
def solve_B(c):
  m = cbrt(c)
  print("Plaintext (m): ",m)
  return m

#fermat attack (p dan q deketan, |p-1|<N^1/4)
def solve_C(N,c):
  e = 65537
  #cari p dan q dengane near consecutive prime exploit menggunakan fermat attack (|p-q| < N ^ 1/4)
  a,_ = gmpy2.iroot(N,2)
  while a*a - N <0:
    a +=1
  b = int(a*a - N)
  sqrt_b,_ = gmpy2.iroot(b,2)
  p = int(a - sqrt_b)
  q = N//p
  phi_p = (p-1) * (q-1)
  d = inverse(e,phi_p)
  m = pow(c,d,N)
  print("Plaintext (m): ",m)
  return m

iteration = int(input("How many iterations? "))
 
# with pwn.process(["python","chall.py"]) as c:
with pwn.remote("34.101.174.85",10004) as c:
  #cetak pesan awalnya
  print(c.recvline())
  for _ in range(iteration):
    #terima datanya
    #mode
    resp = c.recvline()
    mode = resp.decode().split(" ")[-1].strip()
    print(resp) 
    #n
    resp = c.recvline()
    N = int(resp.decode().split(" ")[-1].strip())
    print(resp) 
    # e
    resp = c.recvline()
    e = int(resp.decode().split(" ")[-1].strip())
    print(resp) 
    # c
    resp = c.recvline()
    cipher = int(resp.decode().split(" ")[-1].strip())
    print(resp) 
    #bikin payload
    payload = ""
    if(mode=='A'):
      payload = str(solve_A(N,cipher))
    elif(mode=='B'):
      payload = str(solve_B(cipher))
    elif(mode=='C'):
      payload = str(solve_C(N,cipher))
    # prompt jawaban
    print(c.recvuntil("Your answer: "))
    c.sendline(payload)
    #tunggu responsenya
    print(c.recvline())

  # Lihat responsenya (moga flag)
  response = c.recvall()
  print(response.decode())
```
Program akan menerima jumlah iterasi dan melakukan looping. Di tiap iterasi, program akan menerima data ```mode```,```N```,```e```, dan ```c``` dari server dan melakukan parsing untuk mendapagkan nilainya. Berdasarkan data ```mode``` yang diterima, program akan membuat payload berdasarkan ```mode``` dan data lain yang diberikan. Setelah payload jadi, maka akan dikirimkan ke server. Hal ini berulang hingga iterasi terakhir. 

Setelah iterasi selesai, program akan menerima data dari server sampai socket ditutup agar kita bisa melihat flag-nya.

Ayo kita jalankan!
```
python '.\Rivest Shamir Adleman.py'
```
Masukkan iterasi sebanyak **20**
```
How many iterations?   
```
Dan biarkan program berjalan hingga mendapat flag.
```
[x] Opening connection to 34.101.174.85 on port 10004
[x] Opening connection to 34.101.174.85 on port 10004: Trying 34.101.174.85
[+] Opening connection to 34.101.174.85 on port 10004: Done
b'Starting session.\n'
b'mode = C\n'
b'n = 168684947108466150347013760424249733727123342221721877712989268514445542578711472889784959413133082078651812357366107867053379466665740757669236701597704738965793621218867600151410067223383238196478279816861267667921937928797677899602920187019554450120894068748492119426857379720341571036024798210541488698091\n'
b'e = 65537\n'
b'c = 48514415955462115325786413713271032551370955669651023134007055667717975154594164350732318993913631015715151041661211972069136278098162627667733944175644975624456308460804724480325035943395452014511035332565706199491757273311983452582264107197363504882105532913468458662284946573453056076021063265557107871293\n'
Plaintext (m):  2238451672674540321385179931849208442529547138610346280091876356351210219830
C:\Users\Anugrah  Wiradhika F\Documents\CTF\CTF\Writeup\Compfest\Hacker Class\Cryptography\Rivest Shamir Adleman.py:71: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  print(c.recvuntil("Your answer: "))
b'Your answer: '
C:\Users\Anugrah  Wiradhika F\Documents\CTF\CTF\Writeup\Compfest\Hacker Class\Cryptography\Rivest Shamir Adleman.py:72: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  c.sendline(payload)
b'Correct!\n'
b'mode = C\n'
b'n = 136437835184262877491484956031044972771013263692910012164570734422718653044477696994524424507223652685547867854125641510311516805541267035332690241010011162022489577861306966706449477326252253119181222709229247673161468365604194362567076299288915197904726824626772621246815792254149415966265413287033087250537\n'
b'e = 65537\n'
b'c = 57476846776109479712505767689409478556621383013029370044950715496406248016508073545285656819397827032779359454181755366111912784275377742931715799677463213548371853388983642427193631063710434878545781483472154454471415258255655801011535427738351468084701790756863427004265812838214688410281454672683408584047\n'
Plaintext (m):  32222885637341358336713488641108704774643556866081729664023791386291523489890
b'Your answer: '
b'Correct!\n'
b'mode = C\n'
b'n = 107642796658407310054289751983087818316905930022814925434477703274820801666589347296845501762140286587200440287994246563496594816612336133581371402519498020354546176532826538047943789332121973940537185848227233708086125840256069000575618405393308188126964333766026731178902489229582205895913546180519119797337\n'
b'e = 65537\n'
b'c = 29602615770646590602983878453200223456859184087731716718245734040929451940675641843824370109041620472225231085121023880265705160908660320001480932811160181674912272375627869553066509815162674058812873307199612572158844482515803314767659815878769573185434383569521385797322486870028472560800798644309769158709\n'
Plaintext (m):  74205944516063915138084354617829335725039232022365974649609100284599754507417
b'Your answer: '
b'Correct!\n'
b'mode = C\n'
b'n = 150013817021561646985224626929222660970188316265428427643780989206833032924718688513931139231119711843237459944201440647939874770023578984670492038489294439211384496045216055255354189566595449403635327860443397587038119511039419782236170023386193682111852609782171350627635877083744875015031041549810687999273\n'
b'e = 65537\n'
b'c = 120257924537833037499961210339797012345962512677656939909054195591017887006420585675526926278327313213341380648972431256101967925999981953874422651450873191787902086636039846479004673507609503579373822491822333150095430017421596974668912040744763116959608495425267353531417428933670022141614329057291769169952\n'
Plaintext (m):  35827685984481115436928014157347934249746193507942140071141055869448183089941
b'Your answer: '
b'Correct!\n'
b'mode = C\n'
b'n = 96266057187922083809327406868489645986828883557040889623653568136329503032795709526678418684074070578789471347738451970825026325917619742486049460418278997848921574532926389096729132150826391718945663862830637723228870708806377900723061384295665901514060679541343103128733722149511376607424331426246226168079\n'
b'e = 65537\n'
b'c = 34102846832818586921304489222912753565067014882199075785960853018592933787684626698605565828439846918523514518726981950983778412130437083665897191895659812097838210039327976711013720172859217513581610731413231644918194924411484040912187912114592820895491167774588154224212705082484795022969772408284285967118\n'
Plaintext (m):  81214717707767850781833203063343175317556438219697327562024263976563961694542
b'Your answer: '
b'Correct!\n'
b'mode = C\n'
b'n = 68466695999525660706955078074226301454470071079597802242393032757031069200658112781752065136922945452379610944007369783129740344731089853271903618299938143100940154472896376483485896759095101184442429624056739482779014735312709109936048515735808300448375815987638025318778620450446945675200035922381872489437\n'
b'e = 65537\n'
b'c = 66795147964383342787807879897543336884508503724215450712248782469282542511813874726474156198811393922109762329118380155673383417568810093000567931726320674691978887610402980065731195843655617278431334778263853634772261535428642539914281911696696098199706027312157478335480687824788250808322240603203730811777\n'
Plaintext (m):  98633809286657448589891654020559025874761953155348056405737031070235905697631
b'Your answer: '
b'Correct!\n'
b'mode = A\n'
b'n = 8402406640941798941783574551472570287763829869000901849617388995997807781513560426029626305618391802390532854075955874436899268157948819784934008123927507\n'
b'e = 65537\n'
b'c = 8263239622064770615360649675436922267480161458739206153766578314557461312415461806218197394488913986416354880014204354751359064985142501102034840060748256\n'
Plaintext (m):  49568966446294232202824713725661685688593781968671489849117759380893523999169
b'Your answer: '
b'Correct!\n'
b'mode = B\n'
b'n = 123128689441235164163516736399733954758345700146578829238022999582415977379460445963769947733496747987276196809637015757871699977640041565327240565640672912794388197578075596162420873117263388202469805475842199860992131305716665014487929325233170800952414798882968628583383144176698831043192928050451988567127\n'
b'e = 3\n'
b'c = 547238830901393897908860264380073571665864901831311269806845566205363781232144363548843427363346768622178434615906348022393318769002481401061606387735629326905226981945118657045196025705046566037376707330090425575211735438662614729\n'
Plaintext (m):  81794788820276276616509123652015355119537710462216064955682337058792395698009
b'Your answer: '
b'Correct!\n'
b'mode = A\n'
b'n = 9130696378062305478584120704721591645889003411959198819280800803731490999504776278857242611623944127159640041828002957011127552568198692409602761554851263\n'
b'e = 65537\n'
b'c = 5788847084387566171687001078365548604128652958868758160783983568932293367436007304644070809517113811716481131914198610487789815085482674808476482328420335\n'
Plaintext (m):  52131303809995387948052053192790832914699699610282817349483461386972106406071
b'Your answer: '
b'Correct!\n'
b'mode = B\n'
b'n = 106941883055405278698912254526848169822216111137497063447296453998485447364934277162259951718919240318524537409913682388731550456337195544382562069027163910089133785146881418723537419713126018953095689460177163856475871986636978453475029955938183564333619283039614844799231863983452676554734264526254207937073\n'
b'e = 3\n'
b'c = 1011338499240671339681535397883314390384246259580740221614014741728366512369925416681713272337906639803950954496006460090326588956324628028877715383645981838423133244707381567277627699615189092437465577185122180229907986904169845829\n'
Plaintext (m):  100376530443517771648338239981373089470382750455205180653653352891770344615709
b'Your answer: '
b'Correct!\n'
b'mode = A\n'
b'n = 9360137646547021328134228737744871800297778794439897415217219522393970430484723156895400973782218975991573593851968032219491491538038220758859121067765983\n'
b'e = 65537\n'
b'c = 8924017209720295159191342380226559720937882805923048501916723077130033207182135924331686065988450399113999772993902696558714343834800972246666402539537556\n'
Plaintext (m):  72881802986630764455563054183660492961842588582636402912068650465521675127562
b'Your answer: '
b'Correct!\n'
b'mode = B\n'
b'n = 106778517104661193503085056423716784878028466305664236584896183694023991588206408535727340680116569001899074405483712351036152763694225820346790011886803976908297462621083692432389282248246988499929740522258246898870328926650205298714133786505185308277943586389145441698285866309388519461739028649669638833433\n'
b'e = 3\n'
b'c = 1199933954692829658136960873259323406378392127378050336673459889099266700955000853599600589403458970206731079925744937686915725461405480170491108258863591220067978553325106864756354031272330504491787692628627450301269173598099993088\n'
Plaintext (m):  106263907337726632640808308202143702945728731532256060784244688899491428350792
b'Your answer: '
b'Correct!\n'
b'mode = C\n'
b'n = 72893170232103375828809721986425653412847222883666824160777737526098955026026413241469187420638634545036743110187403834559255932713830265894664329405163847468003913795350818469929333291433291135342795721666223945461928695731033846388614787140695150501368958181904800274982789872501135207559072964768607676501\n'
b'e = 65537\n'
b'c = 53198393889583928815593696620777850648533006899741228950877319156860400260119661479444856148428310645455498776909910127506879523881414885426211300066540160514183213217250325228419632233668324983673141530830807865751504125181621009336503799540589728375917531095131785991654586451789736301652698280431720882373\n'
Plaintext (m):  43821945481627688585247154550353819686842527394501083361748084231564219901433
b'Your answer: '
b'Correct!\n'
b'mode = B\n'
b'n = 112195133722993576593800312988743072613915802195373303299780755417953298012362038818987293560470003072594784153768498040605906067161932134218371453142175402083429444671185297245168938249260437769295599451651389918431811010316381183951424640066600956233939823684951337271932097365266357301304688609628141263959\n'
b'e = 3\n'
b'c = 1360331332637752562207912049510454880807467970152552558637836690915282573450776443747316669715724274660768288319476182873747831140137501501572672137941530416609136089117497758795271322394154391885694989303069681309888232016619637\n'
Plaintext (m):  11080216180443250568047840638985264820177944375577875002739617983728566601133
b'Your answer: '
b'Correct!\n'
b'mode = B\n'
b'n = 155363680274400508056565148123244885342265429113313847681864744951823234631590512583011816780226642512177871789308383125599130225901252245402944143556573866885212569287370977903297560168642690667295905760379710028459317574673806830025257524043104766990014675220804068053335588849594094024367606665029224452697\n'
b'e = 3\n'
b'c = 366805265080293709766864989063335681852704056549341528685954484740669820098429787871809929283333222400472536357590786096071734159310450886026587059804696913176200782813686891064457187982555212169530759346085501251786818047546261\n'
Plaintext (m):  7158332275720407576307294492400481343601288924015989687056281150178127819021
b'Your answer: '
b'Correct!\n'
b'mode = B\n'
b'n = 137040967563773925982763146955309874653181351408351891377468202815669772045824086867428921671958352992970327177663506350012355888949621859927730885310717033556945852134106027771453382965006786381936040385033550262420684397511379461926375056921398443510906839774669661989965909021884596217244420356274348238799\n'
b'e = 3\n'
b'c = 485972845623133514539930775781094786675630869215063867628042913092509195833031773732873090925574006455265263446463858885468124986195444637744218582195998242661711963886869918994495909899747275544156012794344035059948612922507321976\n'
Plaintext (m):  78620777506823952993430959640671121408247200033401672889358582293325633967326
b'Your answer: '
b'Correct!\n'
b'mode = A\n'
b'n = 13359763834692509542308268868445231742010149689601660708783838820637252912989258662785504681754724165830066415092624430385394161744124375004501790595445001\n'
b'e = 65537\n'
b'c = 1061968198099302877316057330737955914870097469716184398767039596427051500245283148215668925108447112517570330212045053679953971238498656521741957354666197\n'
Plaintext (m):  16897973508626848010839742034414674972685474280213576876483563216102597892245
b'Your answer: '
b'Correct!\n'
b'mode = B\n'
b'n = 105527961091480650448289818441518457238877134398405336925430593457660570146545518801310728848341697792055837872462920831055974557011654099033631271213935735174562932930969115597588253193299115285213879152621060662998019093606431864683772249562387583638619313076183751896263749879554760994224507842825968406951\n'
b'e = 3\n'
b'c = 16967044658876584865509164240800788227464747195058271140645014949867549881891193827019525345675517409619891023330182587010115621616167328795883484057603700288437003056928978830522571257753722261546246716650658143488904040970430976\n'
Plaintext (m):  25696189969932887178344051104484040027475136533847425542210800910409177001576
b'Your answer: '
b'Correct!\n'
b'mode = C\n'
b'n = 171736158448860986113765927667915617807832416597874818088702612758862448176154941921613306299276812608760978061337933541626190961869046415483630092505663674135805304682203946100133339495661433163501999057942702566043455505755749611244251285954729634591090206704046132833798217725376035299783417449836003662753\n'
b'e = 65537\n'
b'c = 11294823354862524651072823622127462546964971879680816824432070328187952116390347162690437594689906120912201491459617570921422944222620211962659953217850373402624531472646986289983045676624467473725182354311975188850572642953078193532346588210059749165032256827608723448782702592079286064444484718082971972751\n'
Plaintext (m):  21033711183975756601465739552936177763903341675554317452788046087444990775614
b'Your answer: '
b'Correct!\n'
b'mode = A\n'
b'n = 8674854635646001590112392990465140310219762067886226119406281997982361650233531804311472790722679579239208725243461064293890825323742802703020437669525523\n'
b'e = 65537\n'
b'c = 7486211021683733232467385004360072185966928383298920684091497527415594702800972484822241928082855864952364689131162947116465927134489282461303025085891583\n'
Plaintext (m):  60680596397408573542826835700822612957630146806154204640017273760834255754445
b'Your answer: '
b'Correct!\n'
[x] Receiving all data
[x] Receiving all data: 121B
[+] Receiving all data: Done (121B)
[*] Closed connection to 34.101.174.85 port 10004
Congrats! Here's your flag: COMPFEST15{f4cTOriNG_th3_proDUct_oF_Tw0_LaR6e_PR1me_Is_diFFiCuLt_66bb26e570}
Ending session.
```
Dan...kita dapat flag-nya:
```
COMPFEST15{f4cTOriNG_th3_proDUct_oF_Tw0_LaR6e_PR1me_Is_diFFiCuLt_66bb26e570}
```
### Reflections

Permulaan menarik untuk belajar vulnerability RSA yakni bila nilai ```e``` kecil, ```N``` adalah bilangan prima, serta ```p``` dan ```q``` cukup dekat. Selain itu, _challenge_ ini membantu mengasah skill scripting **python** dan **pwntools**
  

---
[Back to home](../Readme.md)

