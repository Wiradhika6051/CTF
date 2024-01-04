LOWERCASE_OFFSET = ord("a")
ALPHABET = 'abcdefghijklmnop'

def b16_decode(cipher):
	plain = ""
	for i in range(0,len(cipher),2):
		index_lower = ALPHABET.index(cipher[i])
		index_upper = ALPHABET.index(cipher[i+1])
		binary = "{0:08b}".format((index_lower<<4) + index_upper)
		plain += chr(int(binary,2))
	return plain

# cip = ALPHABET[(ord(p) + ord(k) - 2* LOWERCASE_OFFSET) % len(ALPHABET)]
# ALPHABET[i] = cip
# idx(cip) = i
# i = (ord(p) + ord(k) - 2* LOWERCASE_OFFSET) % len(ALPHABET)
# -1 % 16 == 15 % 16
# i + n * (len(ALPHABET)) = ord(p) + ord(k) - 2* LOWERCASE_OFFSET
# ord(p) = i + n * (len(ALPHABET)) - ord(k) + 2* LOWERCASE_OFFSET
# p = chr(i + n * (len(ALPHABET)) - ord(k) + 2* LOWERCASE_OFFSET)
# p = chr(ALPHABET.index(c)  - ord(k) + 2* LOWERCASE_OFFSET + n * (len(ALPHABET)))
# p = chr(term1 + term2)
# term1 = ALPHABET.index(c)  - ord(k) + 2* LOWERCASE_OFFSET
# term2 = n * (len(ALPHABET))
# n = [0..1], 
def reverse_shift(c, k):
	term1 =  ALPHABET.index(c)  - ord(k) + 2* LOWERCASE_OFFSET
	for n in range(2):
		term2 = n * (len(ALPHABET))
		if(ord(ALPHABET[0]) <= (term1 + term2) <= ord(ALPHABET[-1])):
			return chr(term1 + term2)

ciphertext = input("Enter ciphertext:")
keys = list(ALPHABET)
## Key nya 1 karakter antara a sampai p
# assert all([k in ALPHABET for k in key])
# assert len(key) == 1 
#coba semua kemungkinan key
for key in keys:
	plain = ""
	for i, c in enumerate(ciphertext):
		plain += reverse_shift(c, key)
	flag = b16_decode(plain)
	print(f"Key: {key}. Flag: {flag}")