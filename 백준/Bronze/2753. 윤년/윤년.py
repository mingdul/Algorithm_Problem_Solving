year=int(input())

def cal(n):
    leap=""
    if n % 4 ==0 and n%100 !=0:
        leap=1
    elif n%400==0:
        leap=1
    else :
        leap=0
    print(leap)
        
cal(year)