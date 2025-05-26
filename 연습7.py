import tkinter
import tkinter.messagebox

root = tkinter.Tk()
root.title('연습')
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()
bgimg = tkinter.PhotoImage(file='mina.png')
canvas.create_image(400,300,image=bgimg)

def cbtnClick():
    checkNum=0
    if cvalue1.get() == True : checkNum+=1
    answer = tkinter.messagebox.askyesno('컴퓨터 내 모든 과제들을 정말 삭제하시겠습니까?')
    if answer == True: print('과제 바이바이~')
    else: print('휴.')

cvalue1 = tkinter.BooleanVar()
cvalue1.set(False)

cbtn1 = tkinter.Checkbutton(text='아묻따 클릭하세요.',font=('맑은고딕',10), variable=cvalue1, command=cbtnClick)
cbtn1.place(x=404,y=166)




#좌표 생성기
def mouseMove(event):
    x=event.x
    y=event.y

    labelMouse.config(text=str(x)+ ', '+str(y))
    labelMouse.place(x= 1,y= 1)

root.bind('<Motion>', mouseMove)
labelMouse = tkinter.Label(root, text=', ', font=('맑은고딕',10))



root.mainloop()