arr=[]
for _ in  range(9):
    n=int(input())
    arr.append(n)

arr.sort()
total=sum(arr)


for i in range(9):
    for j in range(i+1,9):
        if total-arr[i]-arr[j]==100:
            f,s=arr[i],arr[j]   
            
            
for num in arr:
    if num != f and num != s:
        print(num)
