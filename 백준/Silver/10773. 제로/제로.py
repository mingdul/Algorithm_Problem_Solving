K=int(input())

S=[]
L=[]
for i in range(K):
    L.append(int(input()))
    if L[i]==0:
        S.pop()
    else:
        S.append(L[i])
print(sum(S))