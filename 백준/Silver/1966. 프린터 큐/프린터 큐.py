from collections import deque

T=int(input())

for i in range(T):
    N,M=map(int,input().split())
    q=deque(list(map(int,input().split())))
    idx=deque(list(range(N)))
    cnt=0
    
    while M in idx:
        while max(q)!=q[0]:
            q.append(q.popleft())
            idx.append(idx.popleft())
        cnt+=1
        q.popleft()
        idx.popleft()
    print(cnt)