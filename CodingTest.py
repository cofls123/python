#1.계산기 만들기

#num1 = int(input('숫자1==> '))
#num2 = int(input('숫자2 ==> '))
#
#result1 = num1 + num2
#result2 = num1 - num2
#result3 = num1 * num2
#result4 = num1 / num2
#result5 = num1 ** num2
#result6 = num1 % num2
#
#print(num1, '+', num2, '=', result1)
#print(num1, '-', num2, '=', result2)
#print(num1, '*', num2, '=', result3)
#print(num1, '/', num2, '=', result4)
#print(num1, '**', num2, '=', result5)
#print(num1, '%', num2, '=', result6)


#2.택배 받기

#print('## 택배를 보내기 위한 정보를 입력하세요. ##')
#Name = input('받는 사람: ')
#Adress = input('주소: ')
#
#G = int(input('무게(g): '))
#
#print('\n받는 사람 ==> ', Name)
#print('주소 ==> ', Adress)
#print('배송비 ==> ', G*5, '원')


#3.헬스장

#P1 = int(input('파운드(1b)를 입력하세요 : '))
#P2 = P1*0.453592
#print(P1, '파운드(1b)는 ', P2, '킬로그램(kb)입니다')
#
#K1 = int(input('킬로그램(kg)을 입력하세요 : '))
#K2 = K1*2.204623
#print(K1, '킬로그램(kb)는 ', K2, '파운드(1b)입니다')


#4.편의점 / tkinter, entry(값입력받기 +entry.get() )

#import tkinter
#
#
#def btn_click():
#    Total = 0
#    numB1 = int(Label1EB.get())
#    numB2 = int(Label2EB.get())
#    numS1 = int(Label1ES.get())
#    numS2 = int(Label2ES.get())
#
#    Total = (numS1*1800) + (numS2*1400) - (numB1*500) - (numB2*900)
#
#
##최종 출력
#    Rest = ('오늘 총 매출액은 ' + str(Total) + '원입니다.')
#    RestLabel.config(text=Rest)
#
#
#
##좌표
#def mouseMove(event):
#    x = event.x
#    y = event.y
#
#    labelMouse.config(text=str(x)+','+str(y))
#    labelMouse.place(x=0, y=0)


#기본문
#root = tkinter.Tk()
#root.title('편의점')
#root.geometry('800x500')


#최종 출력 라벨 미리 만들기! => 나중에 config로 값만 수정할 예정
#RestLabel = tkinter.Label(root, text='', font=('맑은 고딕', 10))
#RestLabel.place(x=72, y=300)



##좌표
#root.bind('<Motion>', mouseMove)
#labelMouse = tkinter.Label(root, text=', ', font=('맑은 고딕', 10))



##구입/판매 이름 라벨
#B = tkinter.Label(root, text='구입 수량', font=('맑은 고딕', 10))
#S = tkinter.Label(root, text='판매 수량', font=('맑은 고딕', 10))
#B.place(x=10 , y= 100)
#S.place(x=10 , y= 200)
#
##종류 이름 라벨
#Label1 = tkinter.Label(root, text='캔커피', font=('맑은 고딕', 10))
#Label2 = tkinter.Label(root, text='삼각김밥', font=('맑은 고딕', 10))
#Label1.place(x=75,y=50)
#Label2.place(x=145,y=50)



##구매 물품 엔트리 / width는 들어가는 글자 수 정도 크기 => height는 폰트 크기에 따라 자동 변환
#Label1EB = tkinter.Entry(width=5)
#Label2EB = tkinter.Entry(width=5)
#Label1EB.place(x=75, y=100)
#Label2EB.place(x=145, y=100)
#
##판매 물품 엔트리
#Label1ES = tkinter.Entry(width=5)
#Label2ES = tkinter.Entry(width=5)
#Label1ES.place(x=75, y=200)
#Label2ES.place(x=145, y=200)



##값 넣어놓기
#Label1EB.insert(0,'10')
#Label2EB.insert(0,'10')
#Label1ES.insert(0,'15')
#Label2ES.insert(0,'5')


##버튼
#btn = tkinter.Button(root, text='계산', font=('맑은 고딕', 10), command=btn_click)
#btn.place(x=72, y=15, width=50, height=20)

#root.mainloop()


#5 글자 거꾸로 뒤집기
#strIn = input('원본 문자열 ==> ')
#strOut = ''
#
#i = len(strIn)-1
#
#while i>=0:
#    strOut += strIn[i]
#    i-=1
#
#print('반대 문자열 ==> ', str(strOut))


#PC방
#Age = int(input('나이를 입력 ==> '))
#
#if Age<19:
#    print('집에 갈 시간이네요!\n협조 갑사합니다.') 
#
#else:
#    print('하던 거 하세요~')


#캔버스
import tkinter

root.bind =('<Motion>', mouseMove)

root=tkinter.Tk()
root.title=('캔버스 연습')

canvas = tkinter.Canvas(root, width=800 , height=600 , bg='skyblue')
canvas.pack()

bgimg = tkinter.PhotoImage(file="miko.png")
canvas.create_image(400,300, image = bgimg)


root.mainloop()