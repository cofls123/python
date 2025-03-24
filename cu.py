import tkinter

root = tkinter.Tk()
root.title('CU')
root.geometry('800x400')

D1 = tkinter.Label(root, text='캔 커피', font=('맑은고딕', 10))
D2 = tkinter.Label(root, text='삼각김밥', font=('맑은고딕', 10))
D3 = tkinter.Label(root, text='바나나 우유', font=('맑은고딕', 10))
D4 = tkinter.Label(root, text='도시락', font=('맑은고딕', 10))
D5 = tkinter.Label(root, text='콜라', font=('맑은고딕', 10))
D6 = tkinter.Label(root, text='새우깡', font=('맑은고딕', 10))

N1 = tkinter.Label(root, text='판매 수량', font=('맑은고딕', 10))
N2 = tkinter.Label(root, text='구매 수량', font=('맑은고딕', 10))


D1.place(x=100,y=40)
D2.place(x=160,y=40)
D3.place(x=250,y=40)
D4.place(x=310,y=40)
D5.place(x=380,y=40)
D6.place(x=420,y=40)

N1.place(x=20,y=80)
N2.place(x=20,y=150)

root.mainloop()