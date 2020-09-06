import sympy
import gmpy2

file = open('encrypted.txt', 'r')
c = file.read().split(',')
flag = ""
for c in c:
    for x in range(32, 127):
        d = gmpy2.mpz(int(c) ^ x)
        if(str(d)[-1] == '1' or str(d)[-1] =='9'):
            if(gmpy2.isqrt_rem(d)[1] == 0):
                flag += chr(x)

print(flag)
