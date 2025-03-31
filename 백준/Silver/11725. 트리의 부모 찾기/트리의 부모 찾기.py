import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

N=int(input())
graph=[[] for _ in range(N+1)]
for _ in range(N-1):
    u,v=map(int,input().split())
    
    #루트가 정해져 있지 않기에 양방향으로 해야함
    graph[u].append(v)
    graph[v].append(u)
    
visited=[0]*(N+1)
parent=[-1]*(N+1)

def dfs(u):
    visited[u]=1
    
    # for i in range(1,N+1):
    #     if graph[u][i]==True and visited[i]==0:
    #         parent[i]=u
    #         dfs(i)
    # return parent

    for v in graph[u]:
        if not visited[v]:
            parent[v]=u
            dfs(v)
dfs(1)

for i in range(2,N+1):
    print(parent[i])