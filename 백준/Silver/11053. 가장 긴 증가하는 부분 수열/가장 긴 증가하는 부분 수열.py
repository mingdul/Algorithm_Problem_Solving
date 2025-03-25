N=int(input())
A=list(map(int, input(). split()))

def LIS():
    if N==0:
        return 0
    
    L=0
    M=[0] * (N+1)
    
    for i in range(N):
        l,h=1,L
        while l<=h:
            mid=(l+h)//2
            if A[M[mid]]<A[i]:
                l=mid+1
            else:
                h=mid-1
        new_L=l
        M[new_L]=i
        L=max([L,new_L])
        
    return L

print(LIS())