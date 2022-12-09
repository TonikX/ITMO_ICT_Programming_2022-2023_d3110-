P = input()
ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
CBA = "DEFGHIJKLMNOPQRSTUVWXYZABCdefghijklmnopqrstuvwxyzabc"
u = len(P)
for i in range(u):
    s = P[i]
    if s in ABC:
        n=ABC.index(s)
        print(CBA[n],end='')
    else:
        print(s,end='')

