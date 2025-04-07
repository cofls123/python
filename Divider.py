#GUI는 레이아웃 필수
#콤마는 구분하는 것/ 점은 속해있는 것 (tkinter.Tk)
import tkinter

#버튼 클릭하면 실행하는 함수
def btn_click():
    #값 입력 (글자여서 숫자로 바꿔야 함)
    num1 = int(entry1.get())
    num2 = int(entry2.get())

    #라벨에 넣을 문자열
    str1 = str(num1) + '을(를) ' + str(num2) + '(으)로 나눈 몫은' + str(num1//num2) + '입니다.'
    str2 = str(num1) + '을(를) ' + str(num2) + '(으)로 나눈 나머지은' + str(num1%num2) + '입니다.'

    #라벨 만들기 (결과가 담긴 문자열 1, 2)
    labelRest1 = tkinter.Label(root,text=str1, font=('맑은고딕',10))
    labelRest1.place(x=21,y=86)

    labelRest2 = tkinter.Label(root,text=str2, font=('맑은고딕',10))
    labelRest2.place(x=21,y=110)


#이벤트_실행
def mouseMove(event):
    x = event.x
    y = event.y
    
    #라벨 값 수정(0,0)
    labelMouse.config(text=str(x)+','+str(y))
    #좌표 라벨 위치
    labelMouse.place(x=0,y=90)

    #좌표는 입력칸이나 값이 들어가는 곳에서는 좌표가 0,0으로 리셋됨 (단점)

#tkinter 기본문
root = tkinter.Tk()
root.title('산술 연산자')
root.geometry('400x400')

#이벤트_감지
root.bind('<Motion>', mouseMove)
#이벤트_좌표 내용
labelMouse = tkinter.Label(root, text=', ', font=('맑은고딕',10))


#라벨 만들기 (설명이이 담긴 문자열 1, 2)
label1 = tkinter.Label(root, text='나눠지는 수', font=('맑은고딕', 10))
label2 = tkinter.Label(root, text='나누는 수', font=('맑은고딕', 10))

label1.place(x=20,y=20)
label2.place(x=25,y=45)


#입력칸
entry1 = tkinter.Entry(width=8)
entry2 = tkinter.Entry(width=8)

entry1.place(x=102,y=20)
entry2.place(x=102,y=48)


#계산 버튼 생성
btn = tkinter.Button(root, text='계산', font=('맑은고딕',10), command=btn_click)
btn.place(x=186,y=20,width=54,height=48)

#화면 유지
root.mainloop()


#실행하지 않을 코드는 #붙이면 주석으로 만들어 놓기 (임시저장)
#''' => 여러 문장 주석처리