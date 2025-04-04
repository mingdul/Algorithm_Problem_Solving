N,K=map(int,input().split())

L=list(int(input()) for _ in range(N))

L.sort(reverse=True)
cnt=0
for i in L:
    if K>=i:
        cnt=cnt+(K//i)
        K%=i
print(cnt)  
