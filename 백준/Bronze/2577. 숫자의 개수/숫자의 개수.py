A=int(input())
B=int(input())
C=int(input())
#A,B,C 정수로 입력받고 세수 곱한값을 str로 변경
#0~9까지 반복 #출력값도 반복 for i in range(0부터9) : if list의 원소 == i 합 출력 -> 걍 count 쓰면 됨 ㅋㅋ

mul=str(A*B*C)
for x in range(10):
    sum=mul.count(str(x))
    print(sum)
    