def xor_upto_n(n):
    v = n%8
    if v==0 or v==1:
        return n
    if v==2 or v==3:
        return 2
    if v==4 or v==5:
        return n+2
    return 0

def xorSequence(l, r):
    return xor_upto_n(l-1)^xor_upto_n(r)
