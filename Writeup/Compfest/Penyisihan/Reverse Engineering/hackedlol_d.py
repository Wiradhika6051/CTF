with open('hackedlol.py',"r") as f:
  code = f.read().split('\n')[6:8]
  code[1] = code[1].replace('exec(','decoded =').replace('))',')')
  code.append('for line in decoded.decode().split(";"):')
  code.append(' print(line)')
  with open('hackedlol_temp123.py','w') as t:
      t.write("\n".join(code))