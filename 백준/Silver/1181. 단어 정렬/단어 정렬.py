n=int(input())
L=[]
for _ in range(n):
    L.append(input())

L=list(set(L)) #중복제거 set()함수 ..리스트 형태가 아니기에 감싸줘야함

L.sort()
L.sort(key=len)

for i in L:
    print(i)