# answer = tkinter.messagebox.askyesno('제목','오징어 게임에 참가하시겠습니까?')
#        if answer == True:
#            print('동의')
#        else:
#            print('거절')

#cbtn.getboolean : 안의 값 확인 함수

import tkinter
import random
import tkinter.messagebox

root = tkinter.Tk()
root.title('10주차')
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()

#콤마 기준 8개 항목
result = [
    ' 전생에 고양이였을 가능성은 매우 낮습니다.',
    ' 보통 사람입니다.',
    ' 특별히 이상한 곳은 없습니다.',
    ' 꽤 고양이 다운 구석이 있습니다.',
    ' 고양이와 비슷한 성격 같습니다.',
    ' 고양이와 근접한 성격입니다.',
    ' 전생에 고양이었을지도 모릅니다.',
    ' 겉모습은 사람이지만, 속은 고양이일 가능성이 있습니다.'
]

#체크 버튼 클릭시
def chkBtnClick():
    numCheck = 0 #체크한 개수 확인 변수
    if cvalue1.get() == True: numCheck +=1
    if cvalue2.get() == True: numCheck +=1
    if cvalue3.get() == True: numCheck +=1
    if cvalue4.get() == True: numCheck +=1
    if cvalue5.get() == True: numCheck +=1
    if cvalue6.get() == True: numCheck +=1
    if cvalue7.get() == True: numCheck +=1
    print(numCheck)
    textFiled.delete('1.0',tkinter.END) #값 지우고 넣기
    textFiled.insert('1.0', '<진단결과>\n 당신의 고양이 지수는'+str(int(numCheck/7*100))+'%d입니다. \n'+result[numCheck])
   
#버튼 클릭시
def chkBtnClick():
    numCheck = 0 #체크한 개수 확인 변수
    if cvalue1.get() == True: numCheck +=1
    if cvalue2.get() == True: numCheck +=1
    if cvalue3.get() == True: numCheck +=1
    if cvalue4.get() == True: numCheck +=1
    if cvalue5.get() == True: numCheck +=1
    if cvalue6.get() == True: numCheck +=1
    if cvalue7.get() == True: numCheck +=1
    print(numCheck)
    textFiled.delete('1.0',tkinter.END) #값 지우고 넣기
    textFiled.insert('1.0', ' <진단결과>\n 당신의 고양이 지수는'+str(int(numCheck/7*100))+'%입니다. \n'+result[numCheck])


#캔버스 내 이미지 생성
bgimg = tkinter.PhotoImage(file="mina.png")
canvas.create_image(400,300,image=bgimg)

#이벤트 생성(마우스 커서 좌표)
def mouseMove(event):
    x=event.x
    y=event.y

    labelMouse.config(text=str(x)+', '+str(y))
    labelMouse.place(x=743,y=567)

root.bind('<Motion>', mouseMove)
labelMouse = tkinter.Label(root, text=', ', font=('맑은고딕',10))

#저장 공간 4개 세트
cvalue1 = tkinter.BooleanVar()
cvalue2 = tkinter.BooleanVar()
cvalue3 = tkinter.BooleanVar()
cvalue4 = tkinter.BooleanVar()
cvalue5 = tkinter.BooleanVar()
cvalue6 = tkinter.BooleanVar()
cvalue7 = tkinter.BooleanVar()

cvalue1.set(False)
cvalue2.set(False)
cvalue3.set(False)
cvalue4.set(False)
cvalue5.set(False)
cvalue6.set(False)
cvalue7.set(False)

cbtn1 = tkinter.Checkbutton(text='높은 곳이 좋다', variable=cvalue1)
cbtn2 = tkinter.Checkbutton(text='공을 보면 굴리고 싶어진다', variable=cvalue2)
cbtn3 = tkinter.Checkbutton(text='깜짝 놀라면 털이 곤두선다', variable=cvalue3)
cbtn4 = tkinter.Checkbutton(text='쥐구멍이 마음에 든다', variable=cvalue4)
cbtn5 = tkinter.Checkbutton(text='개에게 적대감을 느낀다', variable=cvalue5)
cbtn6 = tkinter.Checkbutton(text='생선 뼈를 발라 먹고 싶다', variable=cvalue6)
cbtn7 = tkinter.Checkbutton(text='밤, 기운이 난다', variable=cvalue7)

cbtn1.place(x=408, y=162)
cbtn2.place(x=408, y=200)
cbtn3.place(x=408, y=244)
cbtn4.place(x=408, y=286)
cbtn5.place(x=408, y=327)
cbtn6.place(x=408, y=364)
cbtn7.place(x=408, y=404)

#버튼 생성
bnt = tkinter.Button(root, text='진단하기', font=('맑은고딕', 30), bg='lightgreen', command=chkBtnClick)
bnt.place(x=408 ,y=460 ,width=200, height=80)

#텍스트 창
textFiled=tkinter.Text()
textFiled.place(x=330,y=25,width=440,height=110)

root.mainloop()