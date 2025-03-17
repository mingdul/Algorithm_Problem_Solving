import sys
arr=[]
n=int(sys.stdin.readline())

for _ in range(n):
    num=int(sys.stdin.readline())
    arr.append(num)

arr.sort()

for i in arr:
    print(i)