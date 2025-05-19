# test.txt 파일을 읽어와서
# outTest.txt 파일에 작성한다.
#게임 장애물 저장, 게임 스코어 저장, 지금까지 기록한 내용 저장
# 파일 읽어서 쓰기(2)
#strFile = inFile.readlines()
#outFile.writelines(strFile)

inFile = open('test.txt','r')
outFile = open('outTest.txt','w')

# 파일 읽어서 쓰기(1)
while True:
    strFile = inFile.readline()
    #strFile의 값이 없을 때 break
    if (strFile == ''):
        break
    #strFile #암호화 시킨 값 => 저장(strFileChange)
    strFileChange = ''
    for ch in strFile:
        #암호화 / ord() : str => int // chr() : int => str
        chNum = ord(ch)
        chNum = chNum + 100
        chChange = chr(chNum)
        #기록
        strFileChange += chChange 
    outFile.writelines(strFileChange)
print('--------text.txt 암호화 완료--------')

inFile.close()
outFile.close()
