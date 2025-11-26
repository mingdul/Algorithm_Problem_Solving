N,M=map(int,input().split())
lst=[]
for _ in range(N):
    lst.append(list(map(int,input().split())))

dp=[[0]*(M+1) for _ in range(N+1)]
# i=0
# j=0
cnt=0
# while lst[i][j]==0:
#     i+=1
#     j+=1
#     cnt=1
# si=i
# sj=j
# print(dp)
for ci in range(1,N+1):
    for cj in range(1,M+1):
        
        dp[ci][cj]=max((dp[ci-1][cj]),(dp[ci][cj-1]))
        if lst[ci-1][cj-1]==1:
            dp[ci][cj]+=1
print(dp[N][M])