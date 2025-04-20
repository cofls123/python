#실습 1
#팩토리얼 계산기 : 1부터 N까지의 곱

N=5
res=1

for i in range(1,N+1,1):
    res=res*i

#print(res)  #120

#연습1
#1000 - 2000 사이에서 홀수의 합을 구하는 프로그램

res=0

for i in range(1001,2001,2):
    res=res+i
#print(res)


#중첩 for문 / k=0, K=1 한 세트로 3번 작동
for i in range(0,3,1):
    for k in range(0,2,1):
        #print('i: ',i,'   k:',k)
        pass  #에러 안나게 그냥 패스

#실습2
#2단부터 9단까지 구구단을 출력하는 구구단 계산기

for num1 in range(2,10,1): #단
    print('-----구구단',num1,'단------')
    for num2 in range(1,10,1): #곱해지는 수
        print(num1,'X',num2,'=\t', num1*num2)


#while문 / 조건을 무한으로 만듦
while(True):
    num1 = int(input('숫자1 ==> '))
    #num1이 0이면 반복문 종료
    if num1 == 0:
        continue

    num2 = int(input('숫자2 ==> '))
    if num2 == 0:
        continue

    print(num1,'+',num2,'=',num1+num2)


#연습2
#1부터 100까지를 더하되 4의 배수는 더하지 않음
#3의 배수도 더하지 않음

res=0
for i in range(1,101,1):
    if i % 4 == 0:
        continue
    elif i % 3 == 0:
        continue
    res=res+i
print(res)