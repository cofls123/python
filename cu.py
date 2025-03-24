import tkinter

root = tkinter.Tk()
root.title('CU')
root.geometry('900x400')


def btn_click():
    N_num1 = int(entry1.get())
    N_num2 = int(entry2.get())
    N_num2 = int(entry2.get())
    N_num2 = int(entry2.get())
    N_num2 = int(entry2.get())
    N_num2 = int(entry2.get())

#물품
D1 = tkinter.Label(root, text='캔 커피', font=('맑은고딕', 10))
D2 = tkinter.Label(root, text='삼각김밥', font=('맑은고딕', 10))
D3 = tkinter.Label(root, text='바나나 우유', font=('맑은고딕', 10))
D4 = tkinter.Label(root, text='도시락', font=('맑은고딕', 10))
D5 = tkinter.Label(root, text='콜라', font=('맑은고딕', 10))
D6 = tkinter.Label(root, text='새우깡', font=('맑은고딕', 10))

#수량
N1 = tkinter.Label(root, text='판매 수량', font=('맑은고딕', 10))
N2 = tkinter.Label(root, text='구매 수량', font=('맑은고딕', 10))


#물품
D1.place(x=125,y=40)
D2.place(x=240,y=40)
D3.place(x=350,y=40)
D4.place(x=485,y=40)
D5.place(x=610,y=40)
D6.place(x=715,y=40)

#수량
N1.place(x=20,y=100)
N2.place(x=20,y=150)


#판매 수량
D1_N1 = tkinter.Entry(width=4)
D2_N1 = tkinter.Entry(width=4)
D3_N1 = tkinter.Entry(width=4)
D4_N1 = tkinter.Entry(width=4)
D5_N1 = tkinter.Entry(width=4)
D6_N1 = tkinter.Entry(width=4)

#구매 수량
D1_N2 = tkinter.Entry(width=4)
D2_N2 = tkinter.Entry(width=4)
D3_N2 = tkinter.Entry(width=4)
D4_N2 = tkinter.Entry(width=4)
D5_N2 = tkinter.Entry(width=4)
D6_N2 = tkinter.Entry(width=4)


#판매 수량
D1_N1.place(x=130,y=100)
D2_N1.place(x=250,y=100)
D3_N1.place(x=370,y=100)
D4_N1.place(x=490,y=100)
D5_N1.place(x=610,y=100)
D6_N1.place(x=720,y=100)

#구매 수량
D1_N2.place(x=130,y=150)
D2_N2.place(x=250,y=150)
D3_N2.place(x=370,y=150)
D4_N2.place(x=490,y=150)
D5_N2.place(x=610,y=150)
D6_N2.place(x=720,y=150)

btn = tkinter.Button(root, text='계산', font=('맑은고딕',10), command=btn_click)
btn.place(x=80,y=200,width=700,height=30)


root.mainloop()