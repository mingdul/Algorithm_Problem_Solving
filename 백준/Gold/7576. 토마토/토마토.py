from collections import deque

N,M=map(int,input().split())
tomato=[list(map(int,input().split()))for _ in range(M)]
dr=[-1,1,0,0]
dc=[0,0,1,-1]

q=deque() #익은 토마토

# print(tomato)

# graph=[[] for _ in range(N)]
for i in range(M):
    for ii in range(N): 
        if tomato[i][ii]==1: #토마토가 익었다면 큐에 추가
            q.append([i,ii])

#익은 토마토가 없을때까지           
while q:
    length=len(q)
    for _ in range(length):
        #익은 토마토 꺼내기
        r,c=q.popleft()
        #익은 토마토의 인접한 토마토 비교
        for i in range(4):
            nr=r+dr[i]
            nc=c+dc[i]
            
            if nr>=0 and nr<M and nc>=0 and nc<N and tomato[nr][nc]==0:
                tomato[nr][nc]=tomato[r][c]+1
                
                q.append([nr,nc])
        
day=0

for row in tomato:
    for x in row:
        if x==0:
            print(-1)
            exit(0)
    day=max(day,max(row))
    
print(day-1)    
