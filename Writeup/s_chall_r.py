import pwn
from ctypes import CDLL
from ctypes.util import find_library
import time

libc = CDLL(find_library("c"))
 
pwn.context.log_level = 'warn'

CONTEXT = 'remote'

c:pwn.remote|pwn.process = None

def set_context(mode:str)->pwn.remote|pwn.process:
  #mode: 'local','remote'
  if(mode=='remote'):
    return pwn.remote("34.101.89.183", 8020)
  else:
    return pwn.process(["./chall_r"])

def generate_payload(mask,t0,t1):
   PAYLOAD = []
   for i in range(t0,t1+1):
      libc.srand(i)
      temp = libc.rand()
      libc.srand(temp % 0xdf487c4)
      temp2 = libc.rand()
      if((temp2 & 0xff) == (mask[0] ^ ord('C'))):
         print("ketemu. Seed: ",i)
         libc.srand(i)
         break
   #mulai bikin payload
   for i in range(len(mask)):
      temp = libc.rand()
      libc.srand(temp % 0xdf487c4)
      temp2 = libc.rand()
      PAYLOAD.append(chr((mask[i] ^ temp2)&0xff))
   print("".join(PAYLOAD))
   return "".join(PAYLOAD)


if __name__=="__main__":
   #set connection
   t0 = int(time.time())	
   c = set_context(CONTEXT)
   RAW_MASK = c.recvline()
   t1 = int(time.time())
   print(f"Waktu awal: {t0} dan waktu akhir: {t1}")
   MASK = RAW_MASK.rstrip()
   print(MASK)
   # terima prompt
   c.recvuntil("apa mobil kesukaanmu?\n")
   #generate input
   payload = generate_payload(MASK,t0,t1)
   c.sendline(payload)
   print(c.recvline())
  #dapetin 2 pesan input pertama
  #jangan lupa tutup koneksinya
   c.close()
