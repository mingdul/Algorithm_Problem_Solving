#dp에 i번째 동전까지 사용하여 금액 j를 만드는 방법의 수 저장
#금액 0을 만드는 방법은 1가지, 모든행 0열은 1로 초기화

T=int(input())
for _ in range(T):
    n=int(input())
    coins=list(map(int,input().split()))
    w=int(input())
    
    dp=[0 for _ in range(w+1)]
    dp[0]=1
    
    for i in range(n):
        for j in range(coins[i],w+1):
            dp[j]+=dp[j-coins[i]]
    print(dp[w])