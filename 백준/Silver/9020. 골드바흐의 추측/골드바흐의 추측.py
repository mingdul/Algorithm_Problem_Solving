import sys

def find_prime(n): #소수판별함수
    a = [False, False] + [True] * (n - 1)

    # 에라토스테네스의 체 알고리즘으로 소수 찾기
    for i in range(2, int(n**0.5)+1):
        if a[i]:
            for j in range(i * i, n + 1, i):
                a[j] = False
    return a

def pairs(n,primes):
    for i in range(n//2,1,-1):
        if primes[i] and primes[n-i]:
            return(i,n-i)
                
T=int(sys.stdin.readline())
test_cases = []
for _ in range(T):
    n = int(sys.stdin.readline())
    test_cases.append(n)

max_n = max(test_cases)
primes = find_prime(max_n)
    
results = []
for n in test_cases:
    result = pairs(n, primes)
    if result:
        results.append(f"{result[0]} {result[1]}")

for result in results:
    print(result)
