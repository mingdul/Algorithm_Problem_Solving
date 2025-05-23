import sys
input=sys.stdin.readline

N=int(input())
M=int(input())
lst=list(map(int,input().split()))

cnt=0

for i in lst:
    for j in lst:
        if i!=j and i+j==M:

            cnt+=1
        # else:
        #     break
print(cnt//2)