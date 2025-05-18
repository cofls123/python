inFile = open('test.txt','r')
while True:
    strFile = inFile.readline()
    #비어있으면 멈추기
    if (strFile == ''):
        break
    #strFile #암호화 시킨 값 => 저장(strFileChange)
    strFileChange = '' 
    for ch in strFile:
        #암호화
        chNum = ord(ch)
        chNum = chNum - 100
        chChange = chr(chNum)
        #기록 #여기서 더하면 아까 빈칸이었던 곳이 채워지겠지.
        strFileChange += chChange 
    
    print(strFileChange, end="")

inFile.close()