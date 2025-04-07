#기회 9번 / 임의의 숫자 3개 / 숫자 3개 입력

import random



#랜덤 숫자 생성(3개)
secretLen = 3
secretList = random.sample(range(10), secretLen)

#리스트 값을 str으로 변환 후 secret
secret = '' #secretList에서 변환한 값 넣을 자리
for i in range(secretLen):
    secret += str(secretList[i])


#secret 자리에 지금 랜덤으로 숫자 3개가 채워져 있는 상태
#secretLen은 정수값 3


#횟수 제한 9번
for chance in range (9,0,-1):
    while True:
        guess = input('당신의 남은 횟수는 %d번입니다. 추측한 값은? : ' % chance) #guess => input값(입력값)
        if len(guess) == secretLen and guess.isdigit(): #guess의 개수는 secretLen 개수(3개)와 같아야 함 + isdigit(숫자여야 함)
            break
        
        else:
            print('다시 입력하세요.')
            continue

    #스트라이크, 볼 값 올리기
    strike = 0
    ball = 0

    for i in range(secretLen):
        if secret[i] == guess[i]:
            strike += 1
    
        elif guess[i] in secret:
            ball += 1



#스트라이크 / 볼 / 스트라이크+볼 / 아웃
    if strike == secretLen:
        print('정답!')
        break


    #조건
    result = ''

    #스트라이크가 있을 때
    if strike > 0:
        result += '%d strike(s) ' % strike
    
    #볼이 있을 때
    if ball > 0:
        result += '%d ball(s)' % ball

    if result:
        print(result + '\n')

    else:
        print('Out\n')

else:
    print('실패...')