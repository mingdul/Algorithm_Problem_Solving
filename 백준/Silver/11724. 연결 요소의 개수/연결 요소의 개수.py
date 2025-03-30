import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(edge,v, visited):
    visited[v]=True
    for i in edge[v]:
        if not visited[i]:
            dfs(edge, i, visited)
            
N,M=map(int,input().split())
edge=[[] for _ in range(N+1)] #인접리스트를 사용해 각 정점에 직접 연결된 다른 정점들의 리스트를 유지
for _ in range(M):
    u,v=map(int,input().split())
    
    #무방향
    edge[u].append(v)
    edge[v].append(u)
    
cnt=0
visited=[False]* (N+1)
for i in range(1,N+1):
    if not visited[i]:
        dfs(edge,i,visited)
        cnt+=1
        
print(cnt)
