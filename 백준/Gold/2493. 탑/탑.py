import sys

N=int(sys.stdin.readline())
H=list(map(int,sys.stdin.readline().split()))
A = [0] * N
stack = []

for i in range(N):
    while stack and H[stack[-1]] < H[i]:
        stack.pop()
    A[i] = stack[-1] + 1 if stack else 0
    stack.append(i)

print(' '.join(map(str, A)))
