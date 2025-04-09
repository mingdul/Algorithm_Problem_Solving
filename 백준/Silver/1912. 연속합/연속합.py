N=int(input())
#dp[n]=max(dp[n-1]+arr[n],arr[n]) 
#직전까지 연속 합이 양수인 경우 n번째 원소까지 더한 값이 최댓값, 음수인 경우 n번쨰 원소만 있는 경우가 최댓값
arr=list(map(int,input().split()))
dp=[0]*N
dp[0]=arr[0]
for i in range(1,N):
    dp[i]=max(arr[i],dp[i-1]+arr[i])
    # arr[i] 혹은 이전 최대 연속합+arr[i]
print(max(dp))
    