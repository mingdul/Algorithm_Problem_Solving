N=int(input())

def tile(N):
    stack=[1,2]
    for i in range(2,N):
        next=(stack[i-1]+stack[i-2])%10007
        stack.append(next)
    return stack[N-1]

print(tile(N))