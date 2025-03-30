def dfs(v):
    global cnt
    visited[v]=1
    for i in graph[v]:
        if (visited[i]==0):
            dfs(i)
            cnt+=1

    
    
N=int(input())
M=int(input())
graph=[[] for _ in range(N+1)]
cnt=0

for _ in range(M):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
    
visited=[0]*(N+1)
dfs(1)
print(cnt)