n,x=map(int,input().split())

A=[int(x) for x in input().split()]

for i in range(n):
    if x>A[i]:
        print(A[i], end=' ')