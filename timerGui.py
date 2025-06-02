import tkinter

## 전역변수
tmr = 0

## 함수 선언 / 매 시간마다 화면을 채워주는 동영상 만드는 코드
def countUp():
    global tmr
    tmr = tmr + 1
    label['text'] = tmr
    root.after(1000, countUp)  #자신을 호출하면 무한반복 코드 / sec단위

## 메인 함수
root = tkinter.Tk()


root.title('타이머')
root.geometry('300x200')
label = tkinter.Label(text=tmr, font=('궁서체', 80))
label.pack()

countUp()

root.mainloop()