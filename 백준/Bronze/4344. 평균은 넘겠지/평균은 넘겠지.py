c= int(input())
for _ in range(c):
    n=list(map(int,input().split()))
    num=n[0]  #5

    sum_of_list=0
    higer_average=[]
#평균
    for x in range(1,num+1): #1~6
        sum_of_list+=n[x] 
    #평균은 모든 항목의 계산이 끝난 후에 사용되어야 정확한 비교가 가능
    result=sum_of_list/num
    for x in range(1,num+1):
        #비율    
        if n[x]>result:
            higer_average.append(n[x])
            

    ratio=(len(higer_average)/num)*100
    
    
    print(f"{ratio:.3f}%")
