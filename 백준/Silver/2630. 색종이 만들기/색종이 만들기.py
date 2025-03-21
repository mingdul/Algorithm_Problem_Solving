n=int(input())

L=[list(map(int,input().split())) for _ in range(n)]
result=[]

def cut(r,c,n):
    color=L[r][c]
    for i in range(r,r+n):
        for j in range(c,c+n):
            if color != L[i][j]:
                m=n//2
                cut(r,c,m)
                cut(r,c+m,m)
                cut(r+m,c,m)
                cut(r+m,c+m,m)
                return
    if color==0:
        result.append(0)
    else:
        result.append(1)
        
cut(0,0,n)
print(result.count(0))
print(result.count(1))