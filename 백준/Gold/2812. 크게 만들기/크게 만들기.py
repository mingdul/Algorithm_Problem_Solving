n, k = map(int, input().split())
numbers = input().strip()

# 스택 생성
stack = []
# 제거해야 할 숫자의 갯수
remove_count = k

for num in numbers:
    while stack and stack[-1] < num and remove_count > 0:
        stack.pop()
        remove_count -= 1
    stack.append(num)

# 결과는 스택의 처음부터 N-K개의 숫자를 연결한 것
result = ''.join(stack[:n-k])
print(result)