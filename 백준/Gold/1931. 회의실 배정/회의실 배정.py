N=int(input())
lst=[list(map(int,input().split())) for _ in range(N)]
# print(lst)

lst.sort(key=lambda x:(x[1],x[0]))

cnt=0
end_time=0

for s,e in lst:
    if s>=end_time:
        cnt+=1
        end_time=e
print(cnt)
