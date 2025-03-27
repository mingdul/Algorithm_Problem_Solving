L=list(input())
A=list(input())
m=len(A)
stack=[]
for i in L:
    stack.append(i)
    if stack[len(stack)-m:len(stack)]==A:
        for _ in range(m):
            stack.pop()
if stack:
    for i in range(len(stack)):
        print(stack[i], end='')
else:
    print("FRULA")