outFile = open('outTest.txt','w')

while True:
    outStr = input('내용 입력 ==> ')
    #'끝'이라고 입력하면 종료
    if outStr == '끝':
        break
    outFile.writelines(outStr + '\n')
    


outFile.close()