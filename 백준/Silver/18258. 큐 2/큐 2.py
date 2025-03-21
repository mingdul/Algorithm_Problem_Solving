#Queue 시간초과

import sys
from collections import deque

n=int(sys.stdin.readline())
Q=deque([])

for i in range(n):
    L=sys.stdin.readline().split()

    if L[0]=='push':
        Q.append(L[1])
    elif L[0]=='pop':
        if len(Q)==0:
            print(-1)
        else: 
            # Q.pop(0)
            print(Q.popleft())
    elif L[0]=="size":
        print(len(Q))
    elif L[0]=="empty":
        if len(Q)==0:
            print(1)
        else : 
            print(0)
    elif L[0]=="front":
        if len(Q)==0:
            print(-1)
        else :
            print(Q[0])
    else:
        if len(Q)==0:
            print(-1)
        else:
            print(Q[-1]) 