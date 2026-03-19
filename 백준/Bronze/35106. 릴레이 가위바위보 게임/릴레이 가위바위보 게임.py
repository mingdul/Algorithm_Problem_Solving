n=int(input())
l=list(map(int,input().split()))
L=[0]*3
for i in l:
    if i==1:
        L[0]+=1
    if i==2:
        L[1]+=1
    if i==3:
        L[2]+=1

for ii in range(len(L)):
    if L[ii]==min(L):
        a=ii
    if L[ii]==max(L):
        b=ii
print(a+1)
print(b+1)