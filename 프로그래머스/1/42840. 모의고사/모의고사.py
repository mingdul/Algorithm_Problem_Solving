def solution(answers):
    person1=[1,2,3,4,5] * 2000
    person2=[2,1,2,3,2,4,2,5] * 2000
    person3=[3,3,1,1,2,2,4,4,5,5] * 1000
    cnt1=0
    cnt2=0
    cnt3=0
    
    for i in range(len(answers)):
        if answers[i]==person1[i] :
            cnt1+=1

        if answers[i]==person2[i]:
            cnt2+=1

        if answers[i]==person3[i]:
            cnt3+=1
            
    if cnt1>cnt2 and cnt1>cnt3:
        return ([1])
    elif cnt2>cnt1 and cnt2>cnt3:
        return ([2])
    elif cnt3>cnt1 and cnt3>cnt2:
        return ([3])
    elif cnt1==cnt2 and cnt1>cnt3 :
        return ([1,2])
    elif cnt2==cnt3 and cnt2>cnt1:
        return ([2,3])
    elif cnt1==cnt3 and cnt1>cnt2:
        return ([1,3])
    elif cnt1==cnt2==cnt3:
        return [1,2,3]
    

    