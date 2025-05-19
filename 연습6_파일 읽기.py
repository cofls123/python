inFile, outFile = None, None
inStr = ''

inFile=open('연습6.txt', 'r')
while True:
    outStr = input('내용 작성 : ')
    if outStr == '':
        print('필기 끝~')
        break
    inStr+=outStr

    outFile = open('연습6_필기복사.txt', 'w')
    outFile.writelines(inStr+'\n')


inFile.close()
outFile.close()