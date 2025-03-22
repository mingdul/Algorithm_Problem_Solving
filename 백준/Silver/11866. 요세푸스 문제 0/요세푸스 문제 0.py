from collections import deque
N,K=map(int,input().split()) #7,3

# def josephus(n,k):
Q=deque([])
L=[]
for v in range(1,N+1): #1~7
    Q.append(v) #1,2,3,4,5,6,7
        
while len(Q)>1: 
    for i in range(1,K): #1~2
        Q.append(Q.popleft())#3,4,5,6,7,1,2
    L.append(Q.popleft()) #3,6,2,7,5,1
L.append(Q.popleft()) #4

print(f"<{', '.join(map(str,L))}>")