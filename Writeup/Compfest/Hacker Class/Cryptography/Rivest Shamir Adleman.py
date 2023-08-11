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