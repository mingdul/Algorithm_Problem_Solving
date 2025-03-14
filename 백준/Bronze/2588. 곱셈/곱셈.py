num1=int(input())
num2=list(map(int,input().rstrip()))

mul1=num1*num2[2]
mul2=num1*num2[1]
mul3=num1*num2[0]

print(f"{mul1}\n{mul2}\n{mul3}\n{mul1+(mul2*10)+(mul3*100)}")