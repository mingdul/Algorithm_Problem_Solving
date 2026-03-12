N,M=map(int,input().split())
lst=list(map(int,input().split()))
v=[0]*(M+1)
person=[0]*(N)
himang=[]
ans=[]
for i in range(N):
    himang.append(list(map(int,input().split())))
    for j in range(3):
        if v[himang[i][j]-1]<lst[himang[i][j]-1]:
            v[himang[i][j]-1]+=1
            person[i]+=1
            ans.append(himang[i][j])
            break
    if person[i]==0:
        ans.append(-1)
print(*ans)      
    