with open("flag") as f:
   teks = f.read().replace(" ","0").replace(" ","1").replace("\n","")
   binary_chunks = [teks[i:i+8] for i in range(0, len(teks), 8)]

   # Convert each chunk to ASCII character
   ascii_text = ''.join(chr(int(chunk, 2)) for chunk in binary_chunks)

   print(ascii_text)