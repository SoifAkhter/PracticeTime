n, q = map(int, input().split())
entry = [[] for _ in range(n+1)]
dis = [[0]*(n+1) for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int,input().split())
    dis[a][b],dis[b][a] = 1,1
    if entry[a]:
        for i in entry[a]:
            dis[i][b],dis[b][i] = dis[a][i]+1, dis[a][i] +1
            entry[i].append(b)
            entry[b].append(i)
    entry[a].append(b)
    entry[b].append(a)

def dist(x, y):
    if dis[x][y]:
        return dis[x][y]
    else:
        if len(edge[x]) > len(edge[y]):
            x,y = y,x
        return max([(dist(x,a)+dist(a,y)) for a in edge[x]])


def perm(lst):
    per = []
    for i in range(len(lst)-1):
        for j in range(i+1,len(lst)):
            per.append([lst[i],lst[j]])
    return per
for _ in range(q):
    a = int(input())
    if a == 1:
        c = input()
        print(0)
    else:
        stt = list(map(int,input().split()))
        lst = perm(stt)
        sum = 0
        for k in lst:
            sum += k[0]*k[1]*dis[k[0]][k[1]]
        sum %= 10**9 + 7
        print(sum)