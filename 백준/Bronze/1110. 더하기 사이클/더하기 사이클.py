N = input()

def cycle(N):
    Numb = int(N)
    n = Numb 
    cnt = 0
    
    while True:
        num_lst=list(str(Numb)) 
        
        #합
        S = 0
        for i in num_lst:
            S += int(i)
        sum_lst = list(str(S))
        
        new_num = num_lst[-1] + sum_lst[-1]
        Numb = int(new_num)
        
        cnt += 1 

        if Numb == n:
            return cnt

print(cycle(N))

