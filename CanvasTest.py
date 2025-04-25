import tkinter
import random


root = tkinter.Tk()
root.title = ('캔버스 만들기')

#캔버스 생성 / root랑 관련된 canvas를 만들다(객체지향코드)
canvas = tkinter.Canvas(root, width=800, height=600, bg="skyblue")
canvas.pack() #알아서 배치함 (0,0)

#캔버스 내 이미지 생성성(bgimg 변수)
bgimg = tkinter.PhotoImage(file="miko.png")
canvas.create_image(400,300,image=bgimg) #스티커 붙이기(중심점 설정)

#root - canvas - bgimg 연결성 인식(객체지향)


#랜덤 라벨 문자열
def click_btn():
    label['text']=random.choice(['대길','중길','소길','흉'])


#라벨 생성
label = tkinter.Label(root, text='??', font=('맑은고딕', 130))
label.place(x=333 ,y=66 ,width=400, height=200)

#버튼 생성
bnt = tkinter.Button(root, text='제비뽑기', font=('맑은고딕', 30), fg='skyblue', command=click_btn)
bnt.place(x=339 ,y=370 ,width=300, height=100)





#이벤트 생성(마우스 커서 좌표)
def mouseMove(event):
    x=event.x
    y=event.y

    labelMouse.config(text=str(x)+', '+str(y))
    labelMouse.place(x=743,y=567)

root.bind('<Motion>', mouseMove)
labelMouse = tkinter.Label(root, text=', ', font=('맑은고딕',10))

root.mainloop()