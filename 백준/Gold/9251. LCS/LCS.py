X=input()
Y=input()

def LCS(x,y):
    n,m=len(x),len(y)
    dptable=[[0]*(m+1) for _ in range(n+1)] #초기화
            
    for i in range(1,n+1):
        for j in range(1,m+1):
            if x[i-1]==y[j-1]:
                dptable[i][j]=dptable[i-1][j-1]+1
            else:
                dptable[i][j]=max(dptable[i-1][j], dptable[i][j-1])
    return  dptable[n][m]

print(LCS(X,Y))
