import random
import numpy as np

m = np.array([int(open("secret1.txt", "r").read()), int(open("secret2.txt", "r").read())])
r = np.array([[random.getrandbits(100), random.getrandbits(100)], [random.getrandbits(100), random.getrandbits(100)]])
e = np.array([random.getrandbits(100), random.getrandbits(100)])

c = np.dot(e, r) + m
# m = c- np.dot(e,r)
print("r = {}".format(r))
print("c = {}".format(c))

B = Matrix()

# a = np.array([[1,2,],[3,4]])
# b = np.array([5,6])
# print("a.b",np.dot(b,a)) # [23,34]
# 23 = 1 *5 + 3*6
# 34 = 2 *5 + 4*6

#ci = r0i * e0 + r1i * e1 + mi



#ci = r0i * v0 + r1i * v2 + v3


#mi = ci -  r0i * e0 - r1i * e1

#known:
# r0i, r1i, ci

#unknown:
# e0, e1
# print("kalian",np.matmul(a,b))