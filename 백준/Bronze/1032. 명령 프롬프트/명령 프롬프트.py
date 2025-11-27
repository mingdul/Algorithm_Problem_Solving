n=int(input())
file_name=[]
for _ in range(n):
    name=list(input().strip())
    file_name.append(name)
    length=len(name)

diff=list(file_name[0])
lst=[]
for i in range(1,n):

    for j in range(length):
        if file_name[i][j]!=diff[j]:
            diff[j]="?"

for i in range(length):
    
    print(diff[i],end="")