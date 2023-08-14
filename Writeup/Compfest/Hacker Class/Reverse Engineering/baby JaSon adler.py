#baca isi file as binary terus di decode ke utf-8
with open("enc.txt","rb") as f:
    adler_text = f.read().decode()
    print("Read text:",adler_text)

    #karena len(holder1)==len(holder2), maka split jadi 2
    holder1 = adler_text[:len(adler_text)//2]
    print("holder1: ",holder1)

    #pastikan sizenya benar
    assert len(holder1)==len(adler_text)//2

    #reverse holder1 jadi flag
    flag = ""
    for i in range(len(holder1)):
      #kalau indeksnya 0
      if i==0:
         flag += chr(ord(holder1[i]) - 1)
      #buat sisanya
      else:
        #asumsikan karakter terakhir cukup kecil sehingga memenuhi holder1[-1] < ((2 ** 9) << 16)
        flag += chr(ord(holder1[i]) - ord(holder1[i-1]))
    
    #print flag
    print(f"Flag: {flag}")
        