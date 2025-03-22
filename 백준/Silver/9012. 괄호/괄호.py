def make(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return "NO"
            stack.pop()
    return "YES" if not stack else "NO"

T = int(input())
results = []
for _ in range(T):
    ps = input()
    results.append(make(ps))

for result in results:
    print(result)