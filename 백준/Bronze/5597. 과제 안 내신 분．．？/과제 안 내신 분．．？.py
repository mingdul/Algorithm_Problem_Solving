lst=[0]*31
for i in range(28):
    l=int(input())
    lst[l]+=1
for ii in range(1,31):
    if lst[ii] ==0:
        print(ii)
    