import sys
input=sys.stdin.readline
N=int(input())


def tile(n):   
    stack=[1,3]
    if n == 1:
        return stack[0]
    if n == 2:
        return stack[1]
    for i in range(2, n):
        if i % 2 == 0:
            next_value = 2 * stack[i - 1] - 1
        else:
            next_value = 2 * stack[i - 1] + 1
        stack.append(next_value % 10007)
    
    return stack[n - 1]

print(tile(N))
