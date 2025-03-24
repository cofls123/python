#GUI는 레이아웃 필수
#콤마는 구분하는 것/ 점은 속해있는 것 (tkinter.Tk)
import tkinter

def btn_click():
    num1 = int(entry1.get())
    num2 = int(entry2.get())

    str1 = str(num1) + '을(를) ' + str(num2) + '(으)로 나눈 몫은' + str(num1//num2) + '입니다.'
    str2 = str(num1) + '을(를) ' + str(num2) + '(으)로 나눈 나머지은' + str(num1%num2) + '입니다.'


    labelRest1 = tkinter.Label(root,text=str1, font=('맑은고딕',10))
    labelRest1.place(x=21,y=86)

    labelRest2 = tkinter.Label(root,text=str2, font=('맑은고딕',10))
    labelRest2.place(x=21,y=110)

#기본 틀
root = tkinter.Tk()
root.title('산술 연산자')
root.geometry('400x400')


#글자
label1 = tkinter.Label(root, text='나눠지는 수', font=('맑은고딕', 10))
label2 = tkinter.Label(root, text='나누는 수', font=('맑은고딕', 10))

label1.place(x=20,y=20)
label2.place(x=25,y=45)


#입력칸
entry1 = tkinter.Entry(width=8)
entry2 = tkinter.Entry(width=8)

entry1.place(x=102,y=20)
entry2.place(x=102,y=48)


#버튼
btn = tkinter.Button(root, text='계산', font=('맑은고딕',10), command=btn_click)
btn.place(x=186,y=20,width=54,height=48)


root.mainloop()