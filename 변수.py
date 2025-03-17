#/ = 나눗셈
#\ = 파일 경로표현 시 사용

# c = b = a
#a는 b에, b는 c에 들어간다. // b = 100(a) => c = 100(b) *원래의 b값은 덮임
#무조건 오른쪽 계산이 끝난 뒤 등호 왼쪽 변수에 값 대입

#왼쪽에 변수가 하나! but 예외 존재

#ctrl + H

#print = 3 / 예약어를 변수로 사용가능 but print 코드는 사용을 못쓰게 됨

num1 = 100
num2 = 200
resSum = num1 + num2
#로직 생성(변수들의 상호작용)

print(num1,num2,resSum)
print(num1,"+",num2,"=",resSum)

빼기 = num1 - num2
print(num1, '-', num2, '=', 빼기)

곱하기 = num1 * num2
print(num1, 'x', num2, '=', 곱하기)

나누기 = num1 / num2
print(num1, '÷', num2, '=', 나누기)

str1 = "Hello"
str2 = "World"
print(str1, str2)

result = str1 + " " + str2
print(result)

print(str1*5)

#변수 이름을 알아보기 쉽게. 2번째 추천
first_number_of_input_values = 1
firstNumberOfInputValues = 1