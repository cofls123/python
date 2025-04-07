#홀짝 구분분
num = int(input("숫자를 입력 ==> "))

# <- 100 / 100 ~ 1000/ 1000 ->


if num < 100 :
    print("100보다 작음")

elif num < 1000:
    print('1000보다 작고 100보다는 큼')

else:
    print('1000보다 큼')


