import sys
input=sys.stdin.readline
N=int(input())

mat=[]

for _ in range(N):
    r,c=map(int,input().split())
    mat.append((r,c))
    
#n x m, mxk 행렬을 곱하면 행렬 곱셈 비용이 nxmxk
#dp[i][j]는 i+1번째 행부터 j+1번쨰 행렬까지 곱헀을 때의 곱셈 연산 횟수 최소

#dp[i][j]=dp[i][k]+dp[k+1][j] + mat[i][0]*mat[k][1]*mat[j][1]
dp=[[0]*N for _ in range(N)] # dp 초기화

for i in range(N-1):
    dp[i][i+1]=mat[i][0]*mat[i+1][0]*mat[i+1][1] #인접한 행렬 쌍 곱셈비용 계산하여 테이블에 저장, 기본적으로 두 행렬만 곱할 떄 비용의미

# for L in range(2,N):
#     i=0
#     j=N
#     while j<N:
#         dp[i][j]=2**31
#         for k in range(i,j):
#             dp[i][j]=min(dp[i][j],dp[i][k]+dp[k+1][j]+mat[i][0]*mat[k][1]*mat[j][1])
for L in range(2, N):
    for i in range(N-L):
        j = i + L
        dp[i][j] = 2**31  # 또는 float('inf')를 사용
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + mat[i][0] * mat[k][1] * mat[j][1])

        i+=1
        j+=1
print(dp[0][N-1])