import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(parent,x):
    if parent[x]!=x:
        parent[x]=find(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a_root=find(parent,a)
    b_root=find(parent,b)

    if a_root!=b_root:
        parent[b_root]=a_root
        return True
    # print(parent)
    return False

V,E=map(int,input().split())
edge=[]

for _ in range(E):
    a,b,cost=map(int,input().split())
    edge.append((cost,a,b))
    
edge.sort()
parent=[i for i in range(V+1)]
total=0
# print(parent)

for cost,a,b in edge:
    if union(parent,a,b):
        total+= cost

print(total)