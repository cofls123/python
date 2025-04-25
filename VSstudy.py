
#1. 계산기 만들기

#num1 = int(input('숫자1 ==> '))
#num2 = int(input('숫자2 ==> '))

#print(num1, '+', num2, '=' ,num1+num2)
#print(num1, '-', num2, '=' ,num1-num2)
#print(num1, '*', num2, '=' ,num1*num2)
#print(num1, '/', num2, '=' ,num1/num2)
#print(num1, '%', num2, '=' ,num1%num2)
#print(num1, '**', num2, '=' ,num1**num2)



#2. 택배 보내기

#print('## 택배를 보내기 위한 정보를 입력하세요. ##')
#Name = input('받는 사람 : ')
#J = input('주소 : ')
#G = int(input('무게(g) : '))

#print('받는 사람 ==> ', Name)
#print('주소 ==> ', J)
#print('배송비 ==> ', G*5, '원')



#문자열 거꾸로 출력
#strIn = input('원본 문자열 ==> ')  #N자리열
#strOut = strIn[3]+strIn[2]+strIn[1]+strIn[0]
#n = len(strIn)
#print(n)
#print('반대 문자열 ==>', strOut)

#사용자에게 문자열 받기 / while로 n자리 문자열 0의 자리가 될 때까지 반복 / 마지막 문자(n번째)부터 출력
strIn = input('원본 문자열 ==> ')

i = len(strIn) -1 #인덱스는 0부터 시작하므로 -1 => 문자수 != 인덱스(항상 1개가 적어서 없는 숫자가 됨, 즉 인식X)
strOut = ''

while i>=0:
    strOut += strIn[i]
    i-=1
    
print('반대 문자열 ==> ', strOut)

#19세 미만이면 집에 갈 시간이네요. 나이 입력 받고 조건 걸기기(조건문)
#N = int(input('나이를 입력 ==> '))
#if N<19:
#    print('집에 갈 시간이네요!')
#    print('협조 감사합니다.')


