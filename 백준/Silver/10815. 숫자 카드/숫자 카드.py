n=int(input())
A=list(map(int,input().split()))
m=int(input())
B=list(map(int,input().split()))
A.sort()  

def binary(A,key):
    l,r=0,n-1
    
    while l<=r:
        m=(l+r)//2
        if A[m]>key:
            r=m-1
        elif A[m]<key:
            l=m+1
        else :
            return 1
    return 0

for j in B:
    print(binary(A,j), end=' ')