from collections import deque
N,M = map(int,input().split())
lst=[]
for _ in range(M):
    lst.append(list(map(int,input().split())))
    
visited=[[False]*N for _ in range(M)]
dx=[1,0]
dy=[0,1]
jinwoo=deque([[0,0]])
visited[0][0]=True
while jinwoo:
    x,y=jinwoo.pop()
    
    for i in range(2):
        cx=x+dx[i]
        cy=y+dy[i]
        if 0<=cx<N and 0<=cy<M:
            if lst[cy][cx]==1 and visited[cy][cx]==False:
                visited[cy][cx]=True
                jinwoo.append([cx,cy])
            
if visited[-1][-1]==True:
    print("Yes")
else: print("No")
