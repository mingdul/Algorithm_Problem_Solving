def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    sum1=0
    sum2=0
    for i in range(len(A)):
        sum1+=A[i]*B[i-(1+(2*i))]
        sum2+=A[i-(1+(2*i))]*B[i]
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return min(sum1,sum2)