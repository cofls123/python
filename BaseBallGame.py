import tkinter
import tkinter.messagebox as msgbox #메세지 박스 만들기
import random

#좌표 출력기
def mouseMove(event):
    x = event.x
    y = event.y
    labelMouse["text"]=str(x)+","+str(y)

def click_btnCheck():
    global count, btnCheck
    #입력 유효성 확인 / 아무것도 X or 0개 작성 시 return
    if (entryLec1.get() == "") or (entryLec2.get() == "") or (entryLec3.get() == "") :
        return
    elif (len(entryLec1.get()) != 1) or (len(entryLec2.get()) != 1) or (len(entryLec3.get()) != 1):
        return
    
    btnCheck["state"] = "disabled"              #추가 입력 금지
    count += 1                                  #시도 횟수 증가
    successGame = False                         #성공 여부 확인 변수
    #-------------------과제 영역 시작-----------------------#
    #정답인 경우 successGame를 참으로 지정
    #strike = 위치, 숫자
    #ball = 숫자


    strike = 0
    ball = 0

    if (entryLec1.get() == answer[0]) and (entryLec2.get() == answer[1]) and (entryLec3.get() == answer[2]):
        print('정답!')
        successGame = True


    #strike
    if (entryLec1.get() == answer[0]):
        strike = strike+1
    elif (entryLec1.get() == answer[1]) or (entryLec1.get() == answer[2]):
        ball = ball+1

    if (entryLec2.get() == answer[1]):
        strike = strike+1
    elif (entryLec2.get() == answer[0])  or (entryLec2.get() == answer[2]):
        ball = ball+1

    if (entryLec3.get() == answer[2]):
        strike = strike+1
    elif (entryLec3.get() == answer[0]) or (entryLec3.get() == answer[1]):
        ball = ball+1



    output_str = str(strike)+"S"+" "+str(ball)+"B"
    btnCheck["text"] = (output_str)
    #------------------- 과제 영역 끝 -----------------------#

    # Game End (9번의 기회를 모두 사용한 경우)
    if count == 10 :
        response = msgbox.showerror("종료","아쉽게도 모든 기회를 사용했습니다. \n 정답은"+answer+"입니다")
        if response:
            root.destroy()
    
    elif successGame == True:
        response = msgbox.showinfo("성공","정답입니다. \n 정답은"+answer+"입니다")
        if response:
            root.destroy()

    else:
        nextGame()

def nextGame():
    global entryLec1, entryLec2, entryLec3, btnCheck
    labelCount = tkinter.Label(root, text=str(count)+"회", font=("맑은 고딕",10))
    labelCount.place(x=15,y=15+count*25) #배치에도 반복문 활용 가능 / 반복하면서 어떤 변수가 바뀌는지 알아야 함

    entryLec1 = tkinter.Entry(width=2)
    entryLec2 = tkinter.Entry(width=2)
    entryLec3 = tkinter.Entry(width=2)

    entryLec1.place(x=60,y=15+count*25)
    entryLec2.place(x=90,y=15+count*25)
    entryLec3.place(x=120,y=15+count*25)

    btnCheck = tkinter.Button(root, text="확인", font=("Times New Roma",10),command=click_btnCheck)
    btnCheck.place(x=150, y=15+count*25,width=70,height=20)

root = tkinter.Tk()
root.title("야구 게임")
root.geometry("250x270")

#좌표 출력기
root.bind("<Motion>", mouseMove)
labelMouse = tkinter.Label(root, text=",", font=("맑은 고딕",10))
labelMouse.place(x=0,y=250)

#문제 횟수 초기값
count = 1

#문제 제출
answer = str(random.randint(100,999))
print(answer)
while (answer[0] == answer[1]) or (answer[1] == answer[2]) or (answer[0] == answer[2]): #중복되는 숫자가 있는지 비교하는 코드 => 사용자 입력값 비교도 이걸로 사용/ entryLec1(값 입력 변수)
    answer = str(random.randint(100,999))
    print(answer)

nextGame()

root.mainloop()