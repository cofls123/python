import tkinter
root = tkinter.Tk()
root.title = ('캔버스 만들기')
canvas = tkinter.Canvas(root, width=800, height=600, bg="skyblue")


#이벤트 생성(좌표)

def mouseMove(event):
    x=event.x
    y=event.y

    labelMouse.config(text=str(x)+', '+str(y))
    labelMouse.place(x=0,y=90)

root.bind('<Motion>', mouseMove)
labelMouse = tkinter.Label(root, text='제비뽑기', font=('맑은고딕', 10))


#스티커 만들기
bgimg = tkinter.PhotoImage(file="miko.png")
#스티커 붙이기(중심점 설정)
canvas.create_image(400,300,image=bgimg)

#라벨 만들기
Rs = tkinter.Label(root, text='??', font=('맑은고딕', 130))
bnt = tkinter.Button(root, text='제비뽑기', font=('맑은고딕', 30))

#라벨 붙이기기
Rs.place(x=385 ,y=66 ,width=200, height=200)
bnt.place(x=339 ,y=370 ,width=300, height=100)

canvas.pack() #알아서 배치함 (0,0)
root.mainloop()