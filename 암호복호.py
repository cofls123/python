inFile = open('outTest.txt','r')

while True:
    strFile = inFile.readline()
    if (strFile == ''):
        break
    #strFile #암호화 시킨 값 => 저장(strFileChange)
    strFileChange = ''
    for ch in strFile:
        #복호화
        chNum = ord(ch)
        chNum = chNum - 100
        chChange = chr(chNum)
        #기록 
        strFileChange += chChange
    
    print(strFileChange)
    print('--------암호 복호화 완료--------')

outFile = open('outTest.txt','w')
outFile.writelines(strFileChange)

inFile.close()
outFile.close()