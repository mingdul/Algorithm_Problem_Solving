N=int(input())

#총길이, 가운데길이, 순서
def d_c(l,mid,N):
    if N<=3:
        return "moo"[N-1]
    
    left=(l-mid)//2
    
    if N<=left:
        return d_c(left,mid-1,N)
    
    if N>left+mid:
        return d_c(left,mid-1,N-left-mid)
    
    if N-left==1:
        return "m"
    else: 
        return "o"
    
l=3
n=0

while l<N:
    n+=1
    l=2*l+n+3
print(d_c(l,n+3,N))