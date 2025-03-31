import tkinter

root = tkinter.Tk()
root.title('CU')
root.geometry('900x400')


def btn_click():
    SN_num1 = int(D1_SN.get())
    SN_num2 = int(D2_SN.get())
    SN_num3 = int(D3_SN.get())
    SN_num4 = int(D4_SN.get())
    SN_num5 = int(D5_SN.get())
    SN_num6 = int(D6_SN.get())

    BN_num1 = int(D1_BN.get())
    BN_num2 = int(D2_BN.get())
    BN_num3 = int(D3_BN.get())
    BN_num4 = int(D4_BN.get())
    BN_num5 = int(D5_BN.get())
    BN_num6 = int(D6_BN.get())


#총 매출액 = 순이익 - 재고비용
    totalPr = (SN_num1*(1800-500)) + (SN_num2*(1400-900)) + (SN_num3*(1800-800)) + \
    + (SN_num4*(4000-3500)) + (SN_num5*(1500-700)) + (SN_num6*(2000-1000))

    restOb = (SN_num1-BN_num1)*500 + (SN_num2-BN_num2)*900 + (SN_num3-BN_num3)*800 + \
    + (SN_num4-BN_num4)*3500 + (SN_num5-BN_num5)*700 + (SN_num6-BN_num6)*1000
    
    Total = totalPr + restOb


#최종 출력
    str1 = '오늘 총 매출액은' + str(Total) + '원 입니다.'

    labelRest = tkinter.Label(root,text=str1, font=('맑은고딕',10))
    labelRest.place(x=80,y=250)

#물품
D1 = tkinter.Label(root, text='캔 커피', font=('맑은고딕', 10))
D2 = tkinter.Label(root, text='삼각김밥', font=('맑은고딕', 10))
D3 = tkinter.Label(root, text='바나나 우유', font=('맑은고딕', 10))
D4 = tkinter.Label(root, text='도시락', font=('맑은고딕', 10))
D5 = tkinter.Label(root, text='콜라', font=('맑은고딕', 10))
D6 = tkinter.Label(root, text='새우깡', font=('맑은고딕', 10))

#수량
SN = tkinter.Label(root, text='판매 수량', font=('맑은고딕', 10))
BN = tkinter.Label(root, text='구매 수량', font=('맑은고딕', 10))


#물품 키워드 위치
D1.place(x=125,y=40)
D2.place(x=240,y=40)
D3.place(x=350,y=40)
D4.place(x=485,y=40)
D5.place(x=610,y=40)
D6.place(x=715,y=40)

#수량 키워드 위치
SN.place(x=20,y=100)
BN.place(x=20,y=150)



#판매 수량 입력칸
D1_SN = tkinter.Entry(width=4)
D2_SN = tkinter.Entry(width=4)
D3_SN = tkinter.Entry(width=4)
D4_SN = tkinter.Entry(width=4)
D5_SN = tkinter.Entry(width=4)
D6_SN = tkinter.Entry(width=4)

#구매 수량 입력칸
D1_BN = tkinter.Entry(width=4)
D2_BN = tkinter.Entry(width=4)
D3_BN = tkinter.Entry(width=4)
D4_BN = tkinter.Entry(width=4)
D5_BN = tkinter.Entry(width=4)
D6_BN = tkinter.Entry(width=4)



#판매 수량 입력칸 위치
D1_SN.place(x=130,y=100)
D2_SN.place(x=250,y=100)
D3_SN.place(x=370,y=100)
D4_SN.place(x=490,y=100)
D5_SN.place(x=610,y=100)
D6_SN.place(x=720,y=100)

#구매 수량 입력칸 위치
D1_BN.place(x=130,y=150)
D2_BN.place(x=250,y=150)
D3_BN.place(x=370,y=150)
D4_BN.place(x=490,y=150)
D5_BN.place(x=610,y=150)
D6_BN.place(x=720,y=150)

D1_SN.insert(0,"2") #좌표(순번번) , 숫자

#버튼 생성
btn = tkinter.Button(root, text='계산', font=('맑은고딕',10), command=btn_click)
btn.place(x=80,y=200,width=700,height=30)




root.mainloop()