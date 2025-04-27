import tkinter

#좌표 출력기
def mouseMove(event):
    x=event.x
    y=event.y

    labelMouse.config(text=str(x)+ ', '+ str(y)) 
    labelMouse.place(x=10,y=10)


root = tkinter.Tk()
root.title('연습인데용')
root.geometry('700x300')

def btn_click():

    #엔트리값 get 계산
    num1 = int(num1E.get())
    num2 = int(num2E.get())

    result0 = num1 // num2

    #엔트리 값 계산 후 결과 나오는 라벨
    result = tkinter.Label(root, text= num1E.get() + '/'+ num2E.get() + '='+ str(result0))
    result.place(x=100, y=200)

#좌표 출력기
root.bind('<Motion>', mouseMove)
labelMouse = tkinter.Label(root, text='', font=('맑은고딕',10))

#str 글자 라벨 배치
str1 = tkinter.Label(root, text='나누는 수', font=('맑은고딕',10))
str1.place(x=100,y=20)
str2 = tkinter.Label(root, text='나눠지는 수', font=('맑은고딕',10))
str2.place(x=100,y=80)

#엔트리 배치
num1E = tkinter.Entry(width=5)
num1E.place(x=100,y=50)
num2E = tkinter.Entry(width=5)
num2E.place(x=100,y=110)

#버튼
btn = tkinter.Button(root, text='계산! 긔긔!', font=('맑은 고딕',10), command=btn_click)
btn.place(x=194,y=24,width=100,height=50)




#화면유지
root.mainloop()