import tkinter

#좌표출력기
def mouseMove(event):
    x=event.x
    y=event.y

    LabelMouse.config(text=str(x)+', '+ str(y))
    LabelMouse.place(x=5, y=2)
    


root = tkinter.Tk()
root.title('연습 GUI')
root.geometry('600x300')

#버튼 눌렀을 때
#수량 엔트리 가져와서 가격 곱하기 => total
def btn_click():
    total = 0
    SumCanB = int(CanB.get())
    SumCanS = int(CanS.get())
    SumSamB = int(SamB.get())
    SumSamS = int(SamB.get())
    
    #매출액 계산
    total = SumCanS*1800 + SumSamS*1400 - SumCanB*500 - SumSamB*900
    
    #결과 출력
    Result.config(text='오늘 총 매출액은'+str(total)+'원입니다.')

             
Result = tkinter.Label(root, text='',font=('맑은 고딕',10))
Result.place(x=100, y=140)



#좌표 출력기
root.bind('<Motion>', mouseMove)
LabelMouse = tkinter.Label(root, text=', ',font=('맑은 고딕', 10))


#물품 종류 라벨
Can = tkinter.Label(root, text='캔커피',font=('맑은 고딕', 10))
Can.place(x=100,y=10)
Sam = tkinter.Label(root, text='삼각김밥',font=('맑은 고딕', 10))
Sam.place(x=200,y=10)
#구입/판매 라벨
LabelB = tkinter.Label(root, text='구입 수량',font=('맑은 고딕', 10))
LabelB.place(x=20,y=80)
LabelS = tkinter.Label(root, text='판매 수량',font=('맑은 고딕', 10))
LabelS.place(x=20,y=40)

#캔커피 엔트리
CanB = tkinter.Entry(width=5)
CanB.place(x=100, y=40)
CanS = tkinter.Entry(width=5)
CanS.place(x=100, y=80)

#삼김 엔트리
SamB = tkinter.Entry(width=5)
SamB.place(x=200, y=40)
SamS = tkinter.Entry(width=5)
SamS.place(x=200, y=80)

CanB.insert(0,'5')
SamB.insert(0,'5')
CanS.insert(0,'5')
SamS.insert(0,'5')

#버튼
btn = tkinter.Button(root, text='계산~', font=('맑은 고딕',10), command=btn_click)
btn.place(x=101, y=101, width=150, height=20)

root.mainloop()