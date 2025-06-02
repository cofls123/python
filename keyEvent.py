#캐릭터 움직이기 / 

import tkinter

# 전역 변수
key = 0
cx = 400
cy = 300

# 함수 영역
def main_proc():
    global cx, cy
    #lable['text'] = key
    if key == 'Up':
        cy = cy - 20
    if key == 'Down':
        cy = cy + 20
    if key == 'Left':
        cx = cx - 20
    if key == 'Right':
        cx = cx + 20

    canvas.coords('춘식', cx,cy) #이미지를 움직이는 코드 / 키보드 키 값을 받아서 움직이기
    root.after(100,main_proc) #자기 자신을 호출

def key_down(e):
    global key #key 3개가 모두 같은 변수임을 언급
    key = e.keysym #keycode / keysym
    
# 메인 영역
root = tkinter.Tk()
root.title('키 이벤트')
root.bind('<KeyPress>', key_down)
#lable = tkinter.Label(font=('맑은 고딕',80))
#lable.pack()

canvas = tkinter.Canvas(width=800, height=600,bg='skyblue')
canvas.pack()

img = tkinter.PhotoImage(file='춘식.png')
canvas.create_image(400,300, image=img, tag = '춘식')


main_proc()

root.mainloop()