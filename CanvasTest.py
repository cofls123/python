import tkinter
import random


root = tkinter.Tk()
root.title = ('캔버스 만들기')
canvas = tkinter.Canvas(root, width=800, height=600, bg="skyblue")


#랜덤 라벨 문자열
def bnt_click():
    
    Rs.place_forget()

    Bgil = tkinter.Label(root, text='대길', font=('맑은고딕', 100))
    Mgil = tkinter.Label(root, text='중길', font=('맑은고딕', 100))
    Gil = tkinter.Label(root, text='길', font=('맑은고딕', 100))
    Hung = tkinter.Label(root, text='흉길', font=('맑은고딕', 100))

    Bgil.place(x=315 ,y=75 ,width=350, height=200)
    Mgil.place(x=315 ,y=75 ,width=350, height=200)
    Gil.place(x=385 ,y=66 ,width=200, height=200)
    Hung.place(x=385 ,y=66 ,width=200, height=200)

    List=[Bgil, Mgil, Gil, Hung]
    Result=random.choice(List)




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
bnt = tkinter.Button(root, text='제비뽑기', font=('맑은고딕', 30), command=bnt_click)

#라벨 붙이기
Rs.place(x=385 ,y=66 ,width=200, height=200)
bnt.place(x=339 ,y=370 ,width=300, height=100)

canvas.pack() #알아서 배치함 (0,0)
root.mainloop()