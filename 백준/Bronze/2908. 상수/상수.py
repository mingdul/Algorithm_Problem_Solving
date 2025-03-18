n=list(map(int,input().split()))
l=[]

for i in n: #n=[734,893]
    rev=int(str(i)[::-1])
    l.append(rev) #437,398
    
print(max(l))
