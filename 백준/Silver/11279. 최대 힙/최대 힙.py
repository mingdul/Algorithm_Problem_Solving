import heapq
import sys

n=int(sys.stdin.readline())

lst=[]
for _ in range(n):
    x=int(sys.stdin.readline())
    
    if x>0:
        heapq.heappush(lst,-x)
    else:
        if lst:
            L=-heapq.heappop(lst)
            print(L)
        else:
            print(0)