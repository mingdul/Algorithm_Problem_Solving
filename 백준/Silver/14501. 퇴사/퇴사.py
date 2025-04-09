
N = int(input())

ls = []
for _ in range(N):
    ls.append(list(map(int, input().split())))
    
# print(ls)
dp = [0 for _ in range(N+1)]

for i in range(N-1, -1, -1):
    D=ls[i][0]
    W=ls[i][1]
    if i + D > N: # 상담에 필요한 일수가 퇴사일을 넘어가면 전날로 가기
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], W + dp[i + D]) #내일로 넘어감, 오늘 보상+상담이 끝난 다음날부터 최대 수익
        #오늘 상담하면 오늘부터 D일 동안 상담을 못함
        #다음상담은 i+D일부터 가능 
print(dp[0])