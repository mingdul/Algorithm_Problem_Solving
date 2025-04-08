import sys
input=sys.stdin.readline
N=int(input())
graph=[list(map(int, input().split()))for _ in range(N)]

# for a in range(1,N+1):
#     for b in range(1,N+1):
#         graph[a]

# graph=[[]*(N+1) for _ in range(N+1)]

# graph=[list(map(int, input().split()))for _ in range(N)]


for k in range(N):
    for i in range(N):
        for j in range(N):

            if graph[i][j]==1:
                graph[i][j]==graph[i][j]
            else: #graph[i][j]==0
                if graph[i][k]==graph[k][j]==1:
                    graph[i][j]=1
                # else:
                #     graph[i][j]=0
                
for i in range(N):
    print(*graph[i])