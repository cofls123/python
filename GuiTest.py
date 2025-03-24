#import 외부 라이브러리 가져오기
import tkinter


def click_btn():
    labelE = tkinter.Label(root, text='동', font=('돋움', 24))
    labelW = tkinter.Label(root, text='서', font=('돋움', 24))
    labelS = tkinter.Label(root, text='남', font=('돋움', 24))
    labelN = tkinter.Label(root, text='북', font=('돋움', 24))


    labelE.place(x=300,y=200)
    labelW.place(x=100,y=200)
    labelS.place(x=200,y=300)
    labelN.place(x=200,y=100)

    txt = entry.get()
    str1 = txt
    labeltxt = tkinter.Label(root, text=str1, font=('돋움', 24))
    labeltxt.place(x=250,y=350)

root = tkinter.Tk()

root.title('첫 번째 윈도우')  #제목
root.geometry('800x600')  #크기

btn = tkinter.Button(root, text='버튼', font=('돋움', 11),command=click_btn)  #text가 들어가면 폰트 필수
btn.place(x=200,y=200, width=35,height=35)


entry = tkinter.Entry(width=5)  #root 쓸 필요X / width는 입력칸 길이
entry.place(x=200,y=350)


root.mainloop()  #화면이 꺼지지 않게 유지

#Alt + Shift 누른 채 같은 라인 코드 잡기 가능