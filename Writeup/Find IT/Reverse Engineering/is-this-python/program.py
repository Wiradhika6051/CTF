key= "findit2024"
flag_enc = [32,0,0,0,32,32,113,100,116,79,4,89,2,80,54,66,83,92,3,107,8,80,9,11,54,16,93,1,83,90,82,7,49,80,80,71,10,1,1,73]
key_arr = []
for character in key:
   key_arr.append(ord(character))

flag_arr = []
for hex_val in flag_enc:
   flag_arr.append(int(hex_val))

while len(flag_arr) >= len(key_arr):
   key_arr.extend(key_arr)

flag_dec = []
flag_dec = []
for k, f in zip(key_arr, flag_arr):
    xored = k ^ f
    flag_dec.append(xored)

flag_dec_text = ''.join(map(chr, flag_dec))
print(flag_dec_text)
