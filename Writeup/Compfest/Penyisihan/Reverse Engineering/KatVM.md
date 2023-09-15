format:
8 bytes -> jumlah geser

0 -> opcode left + ascii value buat angka nya 
1 -> opcode right + ascii value buat angkanya
2 -> store + jumlah karajter (in hex jumlah angkanya, asumsi 8 bytes) + string
3 -> print
4 -> input
5 -> push 
6 -> popeq + value (buffer char)
7 -> quit

0-7 (hex) -> opcode

indeks 65-18 = 47 dari belakang di push ke stack
[47,31,80,65,77,61,35,88,81,61,38,43,85,39,55,50,54,78,]
