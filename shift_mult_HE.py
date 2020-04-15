import math

def findpow(m):
    return int(math.log(m,2))

t = int(input())
for _ in range(t):
    N,M = map(int,input().split())
    x = []
    while(M):
        a = findpow(M)
        tem = '({}<<{})'.format(N,a)
        x.append(tem)
        M = M - 2**a
    
    print(' + '.join(x))