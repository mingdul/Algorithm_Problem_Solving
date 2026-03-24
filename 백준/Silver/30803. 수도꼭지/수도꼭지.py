import sys
input=sys.stdin.readline
n=int(input())
lst=list(map(int,input().split()))
q=int(input())
v=[1]*(n+1)
temp = list(lst)#save 이전의 물의 양(잠겨서 0 이 될때 다시 수도꼭지 열때 대비)
rst=sum(lst)
print(rst)

for i in range(q):
    jojak=list(map(int,input().split()))
    if jojak[0]==2:
        if v[jojak[1]-1]==1:
            temp[jojak[1]-1]=lst[jojak[1]-1]
            rst-=lst[jojak[1]-1]
            v[jojak[1]-1]=0
            lst[jojak[1]-1]=0

        elif v[jojak[1]-1]==0:
            v[jojak[1]-1]=1
            lst[jojak[1]-1]=temp[jojak[1]-1]
            rst+=lst[jojak[1]-1]
            
    elif jojak[0]==1:
        new_val = jojak[2]
        if v[jojak[1]-1]==1:
            rst += (new_val - lst[jojak[1]-1])
            lst[jojak[1]-1] = new_val
        elif v[jojak[1]-1]==0:
            lst[jojak[1]-1]=0
        temp[jojak[1]-1]=new_val

    print(rst)
