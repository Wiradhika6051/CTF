if __name__=="__main__":
   BUFFER = [' ' for _ in range(200)]
   # print(BUFFER)
   STACK = []
   START=90
   SKIPPED = ['print','store','input','quit']
   with open('source.txt','r') as f:
      pointer = START
      for line in f.readlines():
         subline = line.strip().split(' ')
         if(subline[0] in SKIPPED):
            continue
         # print(subline)
         if(subline[0]=='left'):
            pointer -= int(subline[1])
         elif(subline[0]=='right'):
            pointer += int(subline[1])
         elif(subline[0]=='push'):
            STACK.append(pointer)
            # print("pointer",pointer)
            # print(len(BUFFER))
            BUFFER[pointer] = '~'
         elif(subline[0]=='popeq'):
            BUFFER[STACK[-1]] = subline[1]
            STACK.pop()
      print("".join(BUFFER))