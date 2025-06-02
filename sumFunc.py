#반복되는 부분 함수 사용(수정에 용이)
#코드에 일관성이 형성
def calc(v1, v2, op = '+'):
    result = 0
    if (op == '+'):
        result = v1+v2
    if (op == '-'):
        result = v1-v2
    if (op == '*'):
        result = v1*v2
    if (op == '/'):
        result = v1/v2
    return result
    
op = input('계산입력 (+,-,*,/) : ')
v1 = int(input('첫 번째 숫자 입력 : '))
v2 = int(input('두 번째 숫자 입력 : '))
value = calc(v1,v2)
print('## 계산기 :', v1,op,v2,'=',value)