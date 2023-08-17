import pwn
 
pwn.context.log_level = 'warn'

CONTEXT = 'remote'

c:pwn.remote|pwn.process = None

def set_context(mode:str)->pwn.remote|pwn.process:
  #mode: 'local','remote'
  if(mode=='remote'):
    return pwn.remote("34.101.174.85",10000)
  else:
    return pwn.process(["python3","chall_sf.py"])

def send_payload(payload,block=0):
  #terima pesan awalnya
  c.recvuntil('> ')
  #masukkan input 2
  c.sendline('2')
  #masukkan input payload
  c.sendline(payload)
  #lihat ciphertext
  response = c.recvline()
  ciphertext = response.decode().split(" ")[-1].strip()
  return ciphertext[block*32:(block+1)*32]

def convert_to_hex_str(string:str)->bytes:
  hex_str = string.encode().hex()
  return bytes(hex_str,'utf-8')

if __name__=="__main__":
  FLAG_CHARACTERS = "{}-_!0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

  flags = ""
  #set connection
  c = set_context(CONTEXT)
  #loop terus sampai flag nya complete  (karakter terakhir == '}')
  while len(flags)==0 or  flags[-1]!='}':
    #block yang diperiksa
    block = len(flags) // 16
    #dapetin hash karakter terakhir
    payload = b"00" *  (16 * (block+1) -1 - len(flags)) 
    flag_ciphertext = send_payload(payload,block)
    print("cipher: ",flag_ciphertext)
    #loop semua karakter cari yang cocok
    for char in FLAG_CHARACTERS:
      try_payload = payload + convert_to_hex_str(flags) + convert_to_hex_str(char)
      tried_ciphertext = send_payload(try_payload,block)
      print("try: ",char,"result:",tried_ciphertext)
      if(flag_ciphertext==tried_ciphertext):
        flags += char
        print("FIND MATCH! Current Flag:",flags)
        break
  #jangan lupa tutup koneksinya
  c.close()