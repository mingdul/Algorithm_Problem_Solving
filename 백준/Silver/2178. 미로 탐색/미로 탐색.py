from collections import deque

def bfs():
    Q=deque()
    Q.append((0,0,1))
    v[0][0]=True
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
        
    while Q:
        x,y,cnt=Q.popleft()
        if x==N-1 and y==M-1:
            return cnt
        
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<N and 0<=ny<M and not v[nx][ny] and L[nx][ny]=='1':
                v[nx][ny]=True
                Q.append((nx,ny,cnt+1))
    return -1
                

N,M=map(int,input().split())
#미로
# L=[list(map(int,input().split())) for _ in range(N)]
L=[input() for _ in range(N)]
#방문
v=[[False]*M for _ in range(N)]

result=bfs()
print(result)
