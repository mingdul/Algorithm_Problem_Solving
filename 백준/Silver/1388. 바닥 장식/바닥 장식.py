from collections import deque

N,M=map(int,input().split())
lst=[list(input()) for _ in range(N)]
visited=[[False]*M for _ in range(N) ]

def bfs(u,v):
    Q=deque([(u,v)])

    while Q:
        x,y=Q.popleft()

        if lst[x][y] == '-':
            visited[x][y]==True
            if y+1<M and lst[x][y+1]=='-' and visited[x][y+1]==False:
                Q.append((x,y+1))
                visited[x][y+1]=True
                
        elif lst[x][y]=='|':
            visited[x][y]==True
            if x+1<N and lst[x+1][y]=='|' and visited[x+1][y]==False:
                Q.append((x+1,y))
                visited[x+1][y]=True
cnt=0
for x in range(N):
    for y in range(M):
        if visited[x][y]==False:
            bfs(x,y)
            cnt+=1
            
print(cnt)