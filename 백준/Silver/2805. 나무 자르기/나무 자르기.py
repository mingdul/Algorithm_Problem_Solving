N,M=map(int,input().split())
L=list(map(int,input().split()))
    
def tree(h):
    total=0
    for i in L:
        if i>h:
            total+=i-h
        if total>=M:
            return True
    return False

l, h = 0, max(L)
result=0

while l<=h:
    m=(l+h)//2
    if tree(m):
        result=m
        l=m+1
    else: 
        h=m-1
        
print(result)

