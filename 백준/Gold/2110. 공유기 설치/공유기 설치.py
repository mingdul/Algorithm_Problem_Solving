import sys
input=sys.stdin.readline

n,c=map(int,input().split())
house=[int(input()) for _ in range(n)]

house.sort()

s,e=1,house[-1]-house[0] 

while s<=e:
    mid=(s+e)//2
    current=house[0]
    cnt=1
    for i in range(1,n):
        if house[i]-mid >= current:
            cnt+=1
            current=house[i]
    
    if cnt >=c:
        s=mid+1
        result=mid
    else:
        e=mid-1
print(result)