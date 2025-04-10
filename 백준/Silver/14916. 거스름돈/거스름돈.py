n=int(input())
cnt=0
for i in range(n):
    if ((n-(2*i)) %5) ==0:    
        cnt=i+((n-(2*i))//5)
        break
    else:
        cnt=-1
print(cnt)