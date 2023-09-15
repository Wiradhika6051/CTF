FILENAME = "check.kb"

def parse(data):
   lines = []
   OPCODES_COMMAND = ["left","right","store","print","input","push","popeq","quit"]
   current_opcode = None
   i  = 0
   length = len(data)
   # print(length)
   while i < length:

      if(current_opcode==None and data[i]<8):
         print(lines)
         current_opcode = data[i]
         print(OPCODES_COMMAND[current_opcode])
         if(i<length):
            i+=1
      elif(current_opcode!=None):
         if(current_opcode==0 or current_opcode==1):
            #operasi left atau right
            number_ascii_buffer = []
            while(data[i]>30):
               number_ascii_buffer.append(chr(data[i]))
               if(i<length-1):
                  i+= 1
               else:
                  break
            if(len(number_ascii_buffer)<8):
               while(data[i]==0):
                  # print(i)
                  if(i<length-1):
                     i+=1
                  else:
                     break
            #dapat angkanya
            lines.append(f"{OPCODES_COMMAND[current_opcode]} {''.join(number_ascii_buffer)}")
            #reset opcode
            current_opcode = None
         elif(current_opcode==2):
            #operasi store
            #hitung jumlah karakternya
            number_bin = data[i:i+8]
            i+=8
            size = 0
            # for b in number_bin:
            #    size = (size << 1) | b
            #heuristik: panjang < 356
            size = number_bin[0]
            #dapetin buffernya
            print(size)
            string_buffer = data[i:i+size]
            i+= size
            #dapat angkanya
            lines.append(f"{OPCODES_COMMAND[current_opcode]} {string_buffer.decode()}")
            #reset opcode
            current_opcode = None
         elif((current_opcode>=3 and current_opcode<=5) or current_opcode==7):
            #print, input, push, quit
            lines.append(OPCODES_COMMAND[current_opcode])
            current_opcode = None
            print(current_opcode)
            # if(i<length):
            #    i+=1
            # print(data[i-1],data[i])
         elif(current_opcode==6):
            #opcode 6
            buffer_char = []
            while(data[i]>30):
               buffer_char.append(chr(data[i]))
               if(i<length):
                  i+=1
            #dapat buffernya
            lines.append(f"{OPCODES_COMMAND[current_opcode]} {''.join(buffer_char)}")
            #reset opcode
            current_opcode = None
   return lines

if __name__=="__main__":
   with open(FILENAME,"rb") as f:
      program = f.read()
      instructions = parse(program)
      print(instructions)
      with open("source.txt","w") as s:
         s.write("\n".join(instructions))
