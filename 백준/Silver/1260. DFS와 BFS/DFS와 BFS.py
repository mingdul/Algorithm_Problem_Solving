import sys
input=sys.stdin.readline
n,m,sv=map(int,input().split())

matrix=[[0]*(n+1) for _ in range(n+1)] #인접행렬
for i in range(m):
    s_e,e_e=map(int,input().split())
    matrix[s_e][e_e]=matrix[e_e][s_e]=1
    
visit=[0]*(n+1)
visited=visit.copy()

def dfs(v,path):
    visit[v]=1
    path.append(v)
    for i in range(1,n+1):
        if matrix[v][i]==1 and visit[i]==0:
            dfs(i,path)
    return path

dfs_path=dfs(sv,[])
print(*dfs_path)

def bfs(v,path):
    queue=[v]
    visited[v]=1
    while queue:
        v=queue.pop(0)
        path.append(v)
        for i in range(1,n+1):
            if visited[i]==0 and matrix[v][i]==1 :
                queue.append(i)
                visited[i]=1
    return path

bfs_path=bfs(sv,[])
print(*bfs_path)