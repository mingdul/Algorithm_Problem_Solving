n=int(input())

lst = [[int(x) for x in input().split()]for i in range(n)]

for i in range(n):
    x,y=lst[i]
    print(x+y)
    