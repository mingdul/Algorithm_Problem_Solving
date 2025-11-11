from collections import deque
n=int(input())
house=[]
for _ in range(n):
    lst=list(map(int,input()))
    house.append(lst)

dx=[-1,1,0,0]
dy=[0,0,-1,1]

visited=[[False]*n for _ in range(n)]
# queue=deque()

def bfs(sx,sy):
    queue=deque()
    visited[sx][sy]=True
    queue.append([sx,sy])
    size=1
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny]==False and house[nx][ny]==1:
                    visited[nx][ny]=True
                    queue.append([nx,ny])
                    size+=1
    return size

m_cnt=0
m_size=[]
for i in range(n):
    for j in range(n):
        if house[i][j]==1 and visited[i][j]==False:
            size=bfs(i,j)
            m_size.append(size)
            m_cnt+=1
print(m_cnt)
m_size.sort()
for i in range(len(m_size)):
    print(m_size[i])
            