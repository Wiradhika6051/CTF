from Crypto.Util.number import inverse
from sympy import cbrt,nextprime
import gmpy2
import pwn
 
with pwn.process(["python.exe","chall_sf.py"]) as c:
# with pwn.remote("34.101.174.85",10000) as c:
  #cetak pesan awalnya
  print(c.recvline())
  # for _ in range(iteration):
  #   #terima datanya
  #   #mode
  #   resp = c.recvline()
  #   mode = resp.decode().split(" ")[-1].strip()
  #   print(resp) 
  #   #n
  #   resp = c.recvline()
  #   N = int(resp.decode().split(" ")[-1].strip())
  #   print(resp) 
  #   # e
  #   resp = c.recvline()
  #   e = int(resp.decode().split(" ")[-1].strip())
  #   print(resp) 
  #   # c
  #   resp = c.recvline()
  #   cipher = int(resp.decode().split(" ")[-1].strip())
  #   print(resp) 
  #   #bikin payload
  #   payload = ""
  #   if(mode=='A'):
  #     payload = str(solve_A(N,cipher))
  #   elif(mode=='B'):
  #     payload = str(solve_B(cipher))
  #   elif(mode=='C'):
  #     payload = str(solve_C(N,cipher))
  #   # prompt jawaban
  #   print(c.recvuntil("Your answer: "))
  #   c.sendline(payload)
  #   #tunggu responsenya
  #   print(c.recvline())

  # # Lihat responsenya (moga flag)
  # response = c.recvall()
  # print(response.decode())