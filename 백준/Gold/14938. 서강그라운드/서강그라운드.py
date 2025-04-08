import sys
input=sys.stdin.readline
INF=int(1e9)

N,M,R=map(int,input().split())
t= list(map(int,input().split()))
dist=[[INF]*N for _ in range(N)]

for _ in range(R):
    a,b,l=map(int,input().split())
    dist[a-1][b-1]=l
    dist[b-1][a-1]=l
    
for i in range(N):
    dist[i][i]=0
    
for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
ans=0

for i in range(N):
    rst=0
    for j in range(N):
        if dist[i][j]<=M:
            rst+=t[j]
    ans=max(ans,rst)
print(ans)