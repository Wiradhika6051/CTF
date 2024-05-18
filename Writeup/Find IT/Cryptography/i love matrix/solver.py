import numpy as np
def get_row_matrix(ciphertext,jancok):
    for i in range(10):
      for j in range(10):
         for k in range(10):
            for l in range(10):
               ts = np.array([i,j,k,l],dtype=int).reshape(4,1)
               trying = np.dot(key_2,ts).flatten().real
               # print("C",ciphertext)
               # print(trying % 26)
               c = trying % 26
            #    if(-1<c[0]<1 ):
            #       print("Jancok")
                #   print(c)
            #    if(jancok):
            #       print(c)
               # if(-1<c[0]<1 and 22<c[1]<24 and 2<c[2]<3 and 20<c[3]<22):
               #    print("Jancok")
               #    print(c)
               if(np.allclose(trying % 26,ciphertext)):
                  # Ketemu kombinasinya
                  print("Found")
                  return ts.reshape(1,4).flatten().tolist()
    print("Not found! :sadge:")
    return [0,0,0,0]

# Pecahkan Kunci 2
w = np.loadtxt("data/v.txt",dtype=np.complex128)
v = np.loadtxt("data/w.txt",dtype=np.complex128)
# Reconstruct key
w = np.diag(w)
v_inv = np.linalg.inv(v)
key_2 = (v @ w @ v_inv).real
# Decompile ciphertext
ENC_1_LIST = []
for n in range(1,21):
   print(f"Reading data/encrypted_flag{n}.txt")
   ciphertext = np.loadtxt(f"data/encrypted_flag{n}.txt",dtype=int)
   print(ciphertext)
   # dapatkan row matrix tersebut
   jancok = n == 11
   row_matrix = get_row_matrix(ciphertext,jancok)
   for x in row_matrix:
      ENC_1_LIST.append(str(x))

print(ENC_1_LIST)
# Reverse Encryption 1
total_number = int("".join(ENC_1_LIST))
print(total_number)
# convert ke hex
heksadesimal = total_number.to_bytes((total_number.bit_length() + 7) // 8, 'big')
print(heksadesimal)
# Cari key 1
TEMPLATE= b'FindITCTF{'
key_1 = [TEMPLATE[i] ^ heksadesimal[i] for i in range(len(TEMPLATE))]
# Decode 1
FLAG = []
for i in range(len(heksadesimal)):
   FLAG.append(chr(heksadesimal[i] ^ key_1[i % len(key_1)]))
print(f"Flag: {''.join(FLAG)}")

"""
def encryption2():
    enc2_key = generate_key(4)
    print(enc2_key)
    w, v = np.linalg.eig(enc2_key)

    # np.savetxt("data/v.txt", v)
    # np.savetxt("data/w.txt", w)

    temp = []
    enc2_list = []
    for _ in enc1_list:
        temp.append(_)
        if len(temp) == 4:
            matrix = np.array(temp).reshape(4, 1)
            enc2_list.append(matrix)
            temp = []

    enc2_result = []
    for _ in enc2_list:
        print(_)
        enc2_vec = np.dot(enc2_key, _)
        print(enc2_vec)
        temp = enc2_vec % 26
        print(temp)
        # print(np.linalg.inv(enc2_key)@temp)
        # print((np.linalg.inv(enc2_key)@temp) % 26)
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    for l in range(10):
                        ts = np.array([i,j,k,l],dtype=int).reshape(4,1)
                        trying = np.dot(enc2_key,ts)
                        if(np.all(trying % 26 == temp)):
                            # Ketemu kombinasinya
                            print("Sama")
        # enc2_key_inv = np.linalg.inv(enc2_key)
        # print(np.dot(enc2_key_inv, temp))
        enc2_result.append(temp)
        return enc2_result
    return enc2_result
"""