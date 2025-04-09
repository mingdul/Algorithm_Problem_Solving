import sys
input=sys.stdin.readline
N=int(input())
# def fib(n):
#     if n==1 or n==2:
#         return 1
#     else: return (fib(n-1)+fib(n-2))

def fib2(n):
    f=[0]*(n+1)
    f[1]=f[2]=1
    for i in range(3,n+1):
        f[i]=f[i-1]+f[i-2]
    return f[n]

    # # if n == 0:
    # #     return 0  # 0번째 피보나치 수는 0
    # # elif n == 1:
    # #     return 1
    # stack=[0,1]
    # for i in range(2,n+1):
    #     next=stack[i-1]+stack[i-2]
    #     stack.append(next)
    #     # stack.append(stack[i])
    # return stack[n]    

# 카운터 초기화
count_recursive = 0

# 함수 실행
fib2(N)
count_dynamic = N - 2  # 코드2의 실행 횟수는 (3부터 n까지의 반복 횟수)

# 결과 출력
print(fib2(N), count_dynamic)   
