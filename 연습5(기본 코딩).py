#import tkinter
#import random
#
#root = tkinter.Tk()
#root.title = '캔버스 만들기'
#
#canvas = tkinter.Canvas(root, width=800, height=600, bg='skyblue')
#canvas.pack()
#
#bgimg = tkinter.PhotoImage(file='miko.png')
#canvas.create_image(400,300, image = bgimg)
#
#label = tkinter.Label(root, text='랜덤 돌려돌려~', font=('맑은고딕', 10))
#label.place(x=400,y=200)
#
#root.mainloop()

#계산기
#num1 = int(input('숫자1 ==> '))
#num2 = int(input('숫자2 ==> '))
#
#print(num1, '+', num2, '=', num1+num2)
#print(num1, '-', num2, '=', num1-num2)
#print(num1, '*', num2, '=', num1*num2)
#print(num1, '/', num2, '=', num1/num2)
#print(num1, '%', num2, '=', num1%num2)
#print(num1, '**', num2, '=', num1**num2)


##문자열 거꾸로
#strIn = input('원본 문자열 ==> ')
#strOut = ''
##i 개수는 원본 문자열로 정의 / 반복문 때 하나씩 감소할 예정
#i = len(strIn)-1
#
#
#while i>=0:
#    strOut += strIn[i]
#    i-=1
#
#print('반대 문자열 ==> ' + strOut)

##팩토리얼
#
#N = 5
#res = 1
#
#for i in range(1,N+1,1):
#    res = res*i
#
#print(res)


##구구단
#
#for dan in range(1,10,1):
#    print('----', dan, '단 구구단 시작!----')
#    for i in range(1,10,1):
#        print(dan, 'x', i ,'=\t', dan*i)
#    print('\n')


##1000아래 / 1000-2000사이 / 2000보다 위

#Num = int(input('숫자를 입력하시오 ==> '))
#
#if Num<1000:
#    print('1000보다 작네...')
#elif Num<=2000:
#    print('1000과 2000 사이 숫자군요...? 그죠?')
#
#elif Num>2000:
#    print('2000보다 크네요?')


##3의 배수, 4의 배수 값 빼고 합을 구하자
#N=0
#for i in range(1000,2001,1):
#    if i%3==0:
#        continue
#    if i%4==0:
#        continue
#    N+=i
#print(N)


##주사위 3개의 눈이 다 같아야 함
#import random
#
#dice1 = 0
#dice2 = 0
#dice3 = 0
#count = 0
#
#while (True):
#    dice1 = random.randint(1,6)
#    dice2 = random.randint(1,6)
#    dice3 = random.randint(1,6)
#    count +=1
#
#    if (dice1==dice2) and (dice2==dice3):
#        print('3개의 주사위는 모두두', dice1, '입니다.')
#        print('같은 눈이 나오기까지', count, '번 던졌습니다.')
#        break


##인간과 컴퓨터 대결
#import random
#
#count = 0
#
#while (True):
#    N= random.randint(1,5)
#    guess = int(input('게임'+str(count)+'회: 컴퓨터가 생각한 숫자는? '))
#
#    if N == guess:
#        print('오...이걸 맞추네?')
#        print('종료!!!!')
#        break
#
#    else:
#        print('까비...', N, '였는데~~~~에~~~ 틀렸대요~~')
#        count+=1
#        continue


##문자 찾기
#T = '''
#다시 태어나도
#
#그대를 사랑하고 싶은 것은
#
#한 번이라도 나를 위해 울어준 사람이
#
#바로 그대였기 때문입니다.
#
#그대는 한 번도
#
#그대 자신을 위해 울어본 적이 없는
#
#그렇게도 강인한 사람이었지만
#
#이렇게 연약한 나를 위하여
#
#눈물을 보여주었습니다.
#
#다시 태어나도 
#
#그대를 사랑하고 싶은 것은
#
#이제 내가 그대를 위해
#
#울어줄 차례이기 때문입니다.
#'''
#
#print(T.count('그대'))
#
#i=0
#while (True):
#    num = T.find('그대', i)
#    if num == -1:
#        break
#    
#    print(num)
#    i=num+1


##글자 찾기
#
#text = '''
#사랑은 언제나 오래 참고
#사랑은 온유하며
#사랑은 자랑하지 아니하며
#사랑은 교만하지 아니하며
#사랑은 무례히 행하지 아니하며
#사랑은 자기의 유익을 구하지 아니하며
#사랑은 성내지 아니하며
#사랑은 악한 것을 생각하지 아니하며
#사랑은 불의를 기뻐하지 아니하며
#진리와 함께 기뻐하고
#모든 것을 참으며
#모든 것을 믿으며
#모든 것을 바라며
#모든 것을 견디느니라
#사랑은 언제까지나 떨어지지 아니하되
#'''
#
##num/ i
#i=0
#while (True):
#    num = text.find('사랑', i)
#    if num == -1:
#        break
#    print(num)
#    i=1+num

##홀짝
#number = int(input("숫자 ==> "))
#if number %2 ==0:
#    print('짝수구나!')
#else:
#    print('홀수구나!')


##학점
score = int(input('점수 입력 ==> '))


if score >= 90:
    print('A학점입니다.')
elif score >= 80:
    print('B학점입니다.')
elif score >= 70:
    print('C학점입니다.')
elif score >= 60:
    print('D학점입니다.')

else:
    print('응 F')