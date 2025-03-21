from collections import deque

n=int(input())

D=deque([])

for i in range(1,n+1):
    D.append(i) #1,2,3,4
    
while len(D)>1: #D의 크기가 1보다 작아질때까지
    D.popleft() #1
    F=D[0] #2
    D.append(F) #2,3,4
    D.popleft() 
print(D.popleft())