#읽기 목적으로 파일 열기 / 변수에 저장해서 열려있는 파일 사용
#기존의 텍스트에 줄넘김 기호가 숨어있음 => 이것을 방지하기 위한 end
#텍스트가 끝나면 한 줄 더 출력해도 아무것도 나오지 않음 => 마지막 부분을 확인하기 위해 str가 아무것도 없을 때 경우로 조건문문
#[:-1] => 마지막 한 글자 삭제 / w => 쓰다

import tkinter


root = tkinter.Tk()

file = open('test.txt','r') #encoding = "UTF-8" 텍스트 안뜨면 이 코드 넣기

strFile = file.readline()
root.geometry(strFile[:-1])

strFile = file.readline()
root.title(strFile)

file.close()



root.mainloop()



#readline 한 행씩
'''
while True:
    str = file.readline()
    print(str,end='') 
    if (str == ''):
        break
'''

#readlines 모든 양
'''
fileList = file.readlines()
index = 1

for strList in fileList :
    print(str(index)+' : ' +strList,end="")
    index = index + 1
'''