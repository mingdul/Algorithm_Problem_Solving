import sys
input=sys.stdin.readline
     
T = int(input())

for _ in range(T):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    lst.sort(key=lambda x: x[0])

    cnt = 1 
    best = lst[0][1]

    for i in range(1, N): 
        if lst[i][1] < best: 
            cnt += 1 
            best = lst[i][1] 

    print(cnt)
