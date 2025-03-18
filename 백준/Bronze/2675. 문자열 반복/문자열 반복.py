T = int(input())
for _ in range(T):
    n = input().split()
    R = int(n[0])
    result = ''
    for char in n[1]:
        result += char * R
    print(result)
