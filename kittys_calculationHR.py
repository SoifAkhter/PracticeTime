n, q = map(int, input().split())
edge = [[] for _ in range(n+1)]
dis = [[0]*(n+1) for _ in range(n+1)]

for _ in range(n-1):
    i,j = map(int, input().split())
    edge[i].append(j)
    edge[j].append(i) 
    dis[i][j] = 1

def dist(x, y):
    if dis[x][y]:
        return dis[x][y]
    else:
        if len(edge[x]) > len(edge[y]):
            x,y = y,x
        return max([(dist(x,a)+dist(a,y)) for a in edge[x]])