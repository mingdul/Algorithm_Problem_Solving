N,M=map(int,input().split())
L=[]
for i in range(N):
    L.append(i+1)

for a in range(M):
    i,j=map(int,input().split())
    temp=L[i-1:j]
    temp.reverse()
    L[i-1:j]=temp
for i in range(N):
    print(L[i],end=" ")