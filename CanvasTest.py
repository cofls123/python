import tkinter
root = tkinter.Tk()
root.title = ('캔버스 만들기')
canvas = tkinter.Canvas(root, width=800, height=600, bg="skyblue")

#스티커 만들기
bgimg = tkinter.PhotoImage(file="miko.png")
canvas.create_image(400,300,image=bgimg)


canvas.pack() #알아서 배치함 (0,0)
root.mainloop()