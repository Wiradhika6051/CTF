import pwn
from ctypes import CDLL
from ctypes.util import find_library

libc = CDLL(find_library("c"))

# libc.srand(0x5a35b162)
# print(libc.rand(), libc.rand(), libc.rand())
 
pwn.context.log_level = 'warn'

CONTEXT = 'remote'
# KEY_LEN = 50000

c:pwn.remote|pwn.process = None

def set_context(mode:str)->pwn.remote|pwn.process:
  #mode: 'local','remote'
  if(mode=='remote'):
    return pwn.remote("34.101.89.183", 8020)
  else:
    return pwn.process(["./chall_r"])
  
# def bytes_to_hex(b:bytes):
#   return int(b,16)

def generate_payload(mask,t0,t1):
   PAYLOAD = []
   seed = 0
   for i in range(t0,t1+1):
      libc.srand(i)
      temp = libc.rand()
      libc.srand(temp % 0xdf487c4)
      temp2 = libc.rand()
      if((temp2 & 0xff) == (mask[0] ^ ord('C'))):
         print("ketemu. Seed: ",i)
         libc.srand(i)
         break
   print("lolos")
   #mulai bikin payload
   for i in range(len(mask)):
      temp = libc.rand()
      libc.srand(temp % 0xdf487c4)
      temp2 = libc.rand()
      PAYLOAD.append(chr((mask[i] ^ temp2)&0xff))
   print("".join(PAYLOAD))
      #dapetin initial seed di indeks 0
      # print(mask)
      # print(mask[0])
      # print(ord('C'))
      # initial_seed = mask[0] ^ ord('C')
      # print("TARGET:",initial_seed)
      # a = libc.rand()
      # print(a)
      # print(a ^ ord('C'))
      # xx=int(a ^ ord('C'))
      # print(xx.to_bytes(4,'big'))
      # # print(a)
      # print("GET",(a ^ ord('C'))&0xff)
      # libc.srand(a % 0xdf487c4)
      # b = libc.rand()
   # print(b)
   # print("BB",b&0xff)
   # print("GET 2",(b ^ ord('C'))&0xff)
   # c_ = libc.rand()
   # print("GET",(c_ ^ ord('C'))%0xff)
   # libc.srand(t0-1)
   # d = libc.rand()
   # print("GET",(d ^ ord('C'))%0xff)
   # print(mask[0] ^ ord('C'))
   # c_ = libc.rand()
   # print("GET",(c_ ^ ord('C'))%0xff)
   # libc.srand(t0+1)
   # d = libc.rand()
   # print("GET",(d ^ ord('C'))%0xff)
   # print(mask[0] ^ ord('C'))
   #tes di indeks 1
   # next_seed = lib
#   for i in ran:
#     if()
#     PAYLOAD.append([])
#   return PAYLOAD
   return "".join(PAYLOAD)
import time
import math
if __name__=="__main__":
   #set connection
   t0 = int(time.time())	
   c = set_context(CONTEXT)
   RAW_MASK = c.recvline()
   t1 = int(time.time())
   print(t0,t1)
   MASK = RAW_MASK.rstrip()
   print(MASK)
   # terima prompt
   c.recvuntil("apa mobil kesukaanmu?\n")
   #generate input
   payload = generate_payload(MASK,t0,t1)
   c.sendline(payload)
   print(c.recvline())
  #dapetin 2 pesan input pertama
#   c.recvuntil(b"flag!\n")
#   #dapetin flag yang diencrypt
#   encrypted_flag = c.recvline().rstrip()
#   #tunggu promp input muncul
#   c.recvuntil(b"to encrypt? ")
#   #masukin filler untuk mencapai lokasi mask flag-nya
#   c.sendline(b'\x00' * (KEY_LEN-len(encrypted_flag)//2))
#   #tunggu promp input muncul
#   c.recvuntil(b"to encrypt? ")
#   #masukin payload key-nya
#   c.sendline(b'\x00' * (len(encrypted_flag)//2))
#   # skip tulisan
#   c.recvline()
#   #dapetin responsenya
#   flag_key = c.recvline().rstrip()
#   #decrypt using xor operation
#   flag = []
#   #decode
#   for i in range(0,len(encrypted_flag),2):
#     enc_flag_hex = bytes_to_hex(encrypted_flag[i:i+2])
#     key_hex = bytes_to_hex(flag_key[i:i+2])
#     flag.append(f"{chr(enc_flag_hex ^ key_hex)}")
#   print("This is the flag: picoCTF{" +"".join(flag) + "}")
#   #jangan lupa tutup koneksinya
   c.close()