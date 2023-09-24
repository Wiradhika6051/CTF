import pwn
 
pwn.context.log_level = 'warn'

CONTEXT = 'remote'
KEY_LEN = 50000

c:pwn.remote|pwn.process = None

def set_context(mode:str)->pwn.remote|pwn.process:
  #mode: 'local','remote'
  if(mode=='remote'):
    return pwn.remote("mercury.picoctf.net",36449)
  else:
    return pwn.process(["python","otp.py"])
  
def bytes_to_hex(b:bytes):
  return int(b,16)

if __name__=="__main__":
  #set connection
  c = set_context(CONTEXT)
  #dapetin 2 pesan input pertama
  c.recvuntil(b"flag!\n")
  #dapetin flag yang diencrypt
  encrypted_flag = c.recvline().rstrip()
  #tunggu promp input muncul
  c.recvuntil(b"to encrypt? ")
  #masukin filler untuk mencapai lokasi mask flag-nya
  c.sendline(b'\x00' * (KEY_LEN-len(encrypted_flag)//2))
  #tunggu promp input muncul
  c.recvuntil(b"to encrypt? ")
  #masukin payload key-nya
  c.sendline(b'\x00' * (len(encrypted_flag)//2))
  # skip tulisan
  c.recvline()
  #dapetin responsenya
  flag_key = c.recvline().rstrip()
  #decrypt using xor operation
  flag = []
  #decode
  for i in range(0,len(encrypted_flag),2):
    enc_flag_hex = bytes_to_hex(encrypted_flag[i:i+2])
    key_hex = bytes_to_hex(flag_key[i:i+2])
    flag.append(f"{chr(enc_flag_hex ^ key_hex)}")
  print("This is the flag: picoCTF{" +"".join(flag) + "}")
  #jangan lupa tutup koneksinya
  c.close()