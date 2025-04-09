T=int(input())

def P(N):
    stack=[0,1,1,1,2,2]
    for i in range(6,N+1):
        n=stack[i-5]+stack[i-1]
        stack.append(n)
    return (stack[N])

for i in range(T):
    N=int(input())
    print(P(N))