import sys
import heapq

input= sys.stdin.readline
inf=int(1e9)

N=int(input())
M=int(input())

graph=[[] for _ in range(N+1)]
distance=[inf]*(N+1)

for _ in range(1,M+1):
    u,v,cost=map(int,input().split())
    graph[u].append((v,cost))

s,e=map(int,input().split())

def dijkstra(u):
    q=[]
    heapq.heappush(q,(0,u))
    distance[u]=0
    
    while q:
        dist,curr=heapq.heappop(q)
        
        if distance[curr]<dist:
            #다익스트라 알고리즘은 특정노드를 기준으로 모든 노드에 대한 최단 거리를 구하지만
            #문제에서는 모든 노드가 아닌 end인덱스를 가진 노드에 대한 최단거리만 필요함
            if curr==e:
                break
            else: 
                continue
        
        for n,nc in graph[curr]:
            total=nc+dist
            if distance[n]>total:
                distance[n]=total
                heapq.heappush(q,(total,n))   
    
dijkstra(s) 
print(distance[e])    