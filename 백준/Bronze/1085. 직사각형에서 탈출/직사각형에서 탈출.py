arr=list(map(int,input().split()))

x=arr[2]-arr[0]
y=arr[3]-arr[1]

arr.append(x)
arr.append(y)
print(min(arr))
