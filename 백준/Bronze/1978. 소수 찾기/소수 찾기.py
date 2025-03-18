n = int(input())
L = list(map(int, input().split()))

def is_prime(num):
    if num <= 1:  # 1 이하의 수는 소수가 아니다
        return False
    for i in range(2, int(num**0.5) + 1):  # 2부터 num의 제곱근까지 확인
        if num % i == 0:  # 나누어 떨어지면 소수가 아니다
            return False
    return True  # 나누어 떨어지지 않으면 소수

count = 0
for number in L:
    if is_prime(number):  # 각 수에 대해 소수 판별
        count += 1

print(count)
