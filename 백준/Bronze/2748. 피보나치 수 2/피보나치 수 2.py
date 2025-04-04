from functools import cache
N=int(input())
@cache
def fibo(n):
    if n<=1 : return n
    return fibo(n-1)+fibo(n-2)
r=fibo(N)
print(r)