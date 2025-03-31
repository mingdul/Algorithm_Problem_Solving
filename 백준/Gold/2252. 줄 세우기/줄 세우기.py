from collections import deque
import sys
input=sys.stdin.readline

N,M=map(int,input().split())

indegree=[0]*(N+1)
graph=[[] for _ in range(N+1)]

for i in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)    #[[], [], [], [1], [2]]
    indegree[b]+=1        #[0, 1, 1, 0, 0]

result=[]
q=deque()
    
for i in range(1,N+1):
    if indegree[i]==0:
        q.append(i) #deque([3, 4])

while q:
    tmp=q.popleft()
    result.append(tmp)
    for i in graph[tmp]:
        indegree[i]-=1
        if indegree[i]==0:
            q.append(i)
            
print(*result)