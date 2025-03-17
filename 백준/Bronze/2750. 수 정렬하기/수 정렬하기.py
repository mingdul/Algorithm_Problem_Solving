n=int(input())
arr=[]
for _ in range(n):
    num=int(input())
    arr.append(num)

a=sorted(arr)

for num in a:
    print(num)