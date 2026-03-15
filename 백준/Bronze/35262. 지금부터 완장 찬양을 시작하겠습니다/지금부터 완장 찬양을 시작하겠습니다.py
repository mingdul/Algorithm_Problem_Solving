n,k=map(int,input().split())
lst=list(map(int,input()))
lst.append(2)
cnt=0
f=-1

for i in range(n):
    if lst[i]==0:
        cnt+=1
    if cnt>=k:
        f=0
        break
    else:
        f=1
        
    if lst[i]==0 and lst[i+1]==1:
        cnt=0
        
if f==0:
    print(0)
else:
    print(1)