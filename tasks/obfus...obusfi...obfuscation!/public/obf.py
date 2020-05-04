T = ''
a = chr
B = ord
K = range
c = len
N = print
O = ''.join([a(i+B(T[i])-20)if i % 2 == 0 else a(B(T[i])-i+10)
             for i in K(c(T))])
N(O)
