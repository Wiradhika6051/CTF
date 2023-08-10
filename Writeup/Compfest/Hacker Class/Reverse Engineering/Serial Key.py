import pwn
import string
import math

#jumlah iterasi
iteration = int(input("How many iterations needed? "))
#karakter yang valid
CHARACTER = [str(i) for i in list(range(10))] + list(string.ascii_uppercase)
#hubungkan ke local
max_digit = math.ceil(math.log(iteration,len(CHARACTER)))
with pwn.remote("34.101.174.85",10003) as c:
   #template
   TEMPLATE = "ABCD-EFGH-IJKL-MNOP-QRST"
   #idx buat nandain chara yg perlu di replace
   idx = 0
   for i in range(iteration):
      if(i % len(CHARACTER)==0):
         temp = list(TEMPLATE)
         temp[-max_digit] = CHARACTER[idx]
         TEMPLATE = "".join(temp)
         idx+=1
      print(c.recvuntil("==> "))
      payload = TEMPLATE[:-1] + CHARACTER[i%len(CHARACTER)]
      c.sendline(payload)

   # Lihat responsenya
   response = c.recvall()
   print(response.decode())
