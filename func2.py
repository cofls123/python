def func2():
    global hap           #지역변수 (함수 안에 선언된 변수)가 우선
    result = 100 + num1  #읽기는 가능
    hap = result         #쓰기는 불가능 
    return result

hap = 0
num1 = 10
func2()  #hap에 저장을 안해도 함수만 실행하면 hap에 값이 저장(전역변수)
print(hap)