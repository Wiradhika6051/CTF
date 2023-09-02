with open('important_file.hackedlol','rb') as victim_:
  encrypted_data = victim_.read().decode()
  data = ""
  for i in range(len(encrypted_data)):
    comparator = open('helper.py','r').read()
    data += chr(ord(encrypted_data[i]) ^ ord(comparator[(i*0x27)%len(comparator)]))
  print(data)

              # for victim in range(len(victim_file)):
              #    chr(victim_file[victim]^ord(THIS_FILE[(victim*0x27)%len(THIS_FILE)])