import secrets

import numpy as np
import sympy as sp
# from secret import FLAG

FLAG = "FindITCTF{Halo janc}"


def enc1(message, key):
    return bytes([message[i] ^ key[i % len(key)] for i in range(len(message))])


def encryption1():
    enc1_list = []
    key = secrets.token_bytes(10)
    enc1_result = int(enc1(FLAG.encode(), key).hex(), 16)

    for _ in str(enc1_result):
        enc1_list.append(int(_))

    return enc1_list


def is_coprime(a, b):
    return sp.gcd(a, b) == 1


def generate_key(size):
    while True:
        matrix = np.random.randint(1, 100, size=(size, size))
        det = np.linalg.det(matrix)
        if det != 0 and det % 2 != 0 and det % 13 != 0:
            return matrix


def encryption2():
    enc2_key = generate_key(4)
    print(enc2_key)
    v,w = np.linalg.eig(enc2_key)
    # print(v)
    # print(w)
    W = v
    V = w
    # Reconstruct A
    # V = np.reshape(v,(4,1))
    # V = v
    # print(V)
    # print(W)
    W = np.diag(W)
    V_inv = np.linalg.inv(V)


    # print("Original A:")
    # print(enc2_key)
    reconstructed_A = (V @ W @ V_inv).real
    print(reconstructed_A)
    print(reconstructed_A.astype(int))
    if np.allclose(enc2_key,reconstructed_A):
        print("Masuk")
    # print("\nReconstructed A:")
    # print(reconstructed_A)
    # print(reconstructed_A.real)

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
        enc2_vec = np.dot(enc2_key, _)
        temp = enc2_vec % 26
        enc2_result.append(temp)
    return enc2_result

def get_row_matrix(ciphertext):
   for i in range(10):
      for j in range(10):
         for k in range(10):
            for l in range(10):
               ts = np.array([i,j,k,l],dtype=int).reshape(4,1)
               trying = np.dot(key_2,ts).flatten().astype(int)
               # print("C",ciphertext)
               # print(trying % 26)
               if(np.all(trying % 26 == ciphertext)):
                  # Ketemu kombinasinya
                  print("Found")
                  return ts.reshape(1,4).flatten().tolist()

while True:
    enc1_list = encryption1()
    if len(enc1_list) % 4 == 0:
        break
# print(enc1_list)
enc2_result = encryption2()

# print(enc2_result)
# print(enc2_result[0])
# i = 1
# for _ in enc2_result:
#     np.savetxt("data/encrypted_flag" + str(i) + ".txt", _)
#     i += 1
