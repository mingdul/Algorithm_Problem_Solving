import sys
input = sys.stdin.readline

n=int(input())
L=sorted(list(map(int, input().split())))

##two pointer
s=0
e=n-1

dis=abs(L[s]+L[e]) #0까지의 거리
result=[L[s], L[e]] #초기값

while s<e:
    l=L[s]
    r=L[e]

    total=l+r
    if abs(total) < dis:
        dis=abs(total)
        result=[l,r]
        if dis==0:
            break
    if total<0:
        s+=1
    else:
        e-=1
print(result[0],result[1])