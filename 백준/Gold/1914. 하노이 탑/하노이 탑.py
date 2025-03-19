def hannoi(n,L,M,H):
    if n==1:
        print(L,H,sep=" ")
    else:
        hannoi(n-1,L,H,M)
        hannoi(1,L,M,H)
        hannoi(n-1,M,L,H)
a=int(input())
print(2**a-1)
if(a<=20):
    hannoi(a,1,2,3)