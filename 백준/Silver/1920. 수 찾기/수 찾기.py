N=int(input())
A=list(map(int,input().split()))
M=int(input())
B=list(map(int,input().split()))
#B의 원소들이 A에 존재하는가

def binary(A,key):
    l, r= 0, N-1

    while l<=r:
        m=(l+r)//2
        if A[m]<key:
            l=m+1
        elif A[m]>key:
            r=m-1
        else: return True
    return False
    

def bin_search(A,B):
    A.sort()
    for i in B:
        if binary(A,i):
            print(1)
        else :
            print(0)

bin_search(A,B)
