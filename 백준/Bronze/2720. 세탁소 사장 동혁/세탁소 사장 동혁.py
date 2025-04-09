T=int(input())

c=[25,10,5,1]

for _ in range(T):
    coin=int(input())
    rst=[]
    
    for i in c:
        rst.append(coin//i)
        #거스름돈 C를 현재 동전 가치 i로 나눈 몫 계산, 현재 동전을 최대 몇개 사용할 수 있는지를 나타냄
        coin=coin%i #나머지를 다시 coin에 저장
    print(*rst)