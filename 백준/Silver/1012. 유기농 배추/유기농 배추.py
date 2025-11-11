from collections import deque
T=int(input())

for _ in range(T):
    m,n,k=map(int,input().split())
 
    visited=[[False]*m for _ in range(n)]
    matrix=[[0]*m for _ in range(n)]
    
    for _ in range(k):
        x,y=map(int,input().split())
        # print(x,y)
        matrix[y][x]=1

    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    cnt=0
    # queue=deque()
    for x in range(n):
        for y in range(m):
            if matrix[x][y]==1 and not visited[x][y]:
                cnt+=1
                queue=deque()
                visited[x][y]=True
                queue.append([x,y])
                while queue:
                    c_x,c_y=queue.popleft()
                    for i in range(4):
                        nx=c_x+dx[i]
                        ny=c_y+dy[i]
                
                        if 0<=nx<n and 0<=ny<m:
                            if visited[nx][ny]==False and matrix[nx][ny]==1:
                                visited[nx][ny]=True
                                queue.append([nx,ny])
                            # cnt+=1
    print(cnt)