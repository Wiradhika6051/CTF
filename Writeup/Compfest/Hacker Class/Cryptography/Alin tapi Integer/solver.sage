import numpy as np
r = np.array([[1148260253752960666411026955982 ,1152853384449195147441103181809],
 [531286261948311003070916961777 ,315004570177689845888128427159]]) * -1
c = np.array([1382837223529433249865880805057517251915619710567990062916431,
 1316535860531446525236099898143306829501741219648966991591354]) * -1

B = Matrix([
    [c[0],c[1],1],
    [r[0][0],r[0][1],0],
    [r[1][0],r[1][1],0]
])
l = B.LLL()
print("Result:\n",l)
row = l[0]
m = [abs(row[0]),abs(row[1])]
print("m: ",e)
print("flag: COMPFEST15{"+str(m[0]*m[1])+"}")

"""
Result:
 [               -3613685534                -1042184440                          1]
[ 1868913591731490884035802 -6480298255030202357053827  2784439343230504758092358]
[-1207895475265467573661199  4188274403365901185876888  8087357124767417056183182]
m:  e
flag: COMPFEST15{3766126834587890960}
"""