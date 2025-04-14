#위상정렬

import sys
import heapq
input=sys.stdin.readline

N,M=map(int,input().split())
graph=[[] for _ in range(N+1)]
indegree=[0 for _ in range(N+1)]

Q=[]
result=[]

for i in range(M):
    A,B=map(int,input().split())
    graph[A].append(B)
    indegree[B]+=1
    
for i in range(1,N+1):
    if indegree[i]==0:
        heapq.heappush(Q,i)    

while Q:
    n=heapq.heappop(Q)    
    print(n,end=' ')
    for i in graph[n]:
        indegree[i]-=1
        if indegree[i]==0:
            heapq.heappush(Q,i)
  