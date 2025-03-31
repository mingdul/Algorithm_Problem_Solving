from collections import deque
import sys
input=sys.stdin.readline
def bfs(s):
    Q=deque()
    Q.append(s)
    visited=[False]*(N+1)
    dist=[-1]*(N+1)
    visited[s]=True
    dist[s]=0
    
    while Q:
        v=Q.popleft()
        for i in graph[v]:
            if visited[i]==False:
                visited[i]=True
                dist[i]=dist[v]+1
                Q.append(i)
    result=[]
    for i in range(1,N+1):
        if dist[i]==K:
            result.append(i)
    return result if result else [-1] 
    # if result:
    #     return result
    # else:
    #     return -1
    
    
N,M,K,X=map(int,input().split())
graph=[[] for _ in range(N+1)]
for _ in range(M):
    s,e=map(int,input().split())
    graph[s].append(e)

result=bfs(X)

if result == [-1]:  # This checks if the result is the special [-1] indicating no cities found
    print(-1)
else:
    for city in result:
        print(city)