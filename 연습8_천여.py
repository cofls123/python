#input 또는 print 3회 이상 사용 / 30줄 이상 코드 / 조건문 2개 이상 / 반복문 2개 이상
#퀴즈게임 / 반복문1: 목숨 3개, 반복문2: 퀴즈 풀 때까지 반복 / 조건문: 퀴즈문제

print('---영단어 퀴즈를 시작합니다.---')

heart = 3
score = 0

while heart > 0:
    Q1 = input('개 : ')
    if Q1 == 'dog':
        print('정답! 개 : dog')
        score+=1
        break
    else:
        print('오답!')
        heart-=1
        print('하트가', heart, '개 남았습니다.')
    if heart == 0:
        break

while heart > 0:
    Q2 = input('고양이 : ')
    if Q2 == 'cat':
        print('정답! 고양이 : cat')
        score+=1
        break
    else:
        print('오답!')
        heart-=1
        print('하트가', heart, '개 남았습니다.')
    if heart == 0:
        break

#OX퀴즈
while heart > 0:
    Q3 = input('새 : birth (O/X) ')
    if Q3 == 'X':
        print('X 정답!')
        score+=0.5
        A = input('그럼 올바른 철자는? ')
        if A=='bird':
            print('정답! 새 : bird')
            score+=0.5
            break
        else:
            print('오답')
            heart-=1
            print('하트가', heart, '개 남았습니다.')
            continue
        
    if Q3 == 'O':
        print('O 오답!')
        heart-=1
        print('하트가', heart, '개 남았습니다.')
    else:
        print('O 또는 X를 입력해주세요.')
            
#하트가 0개가 되면 종료
    if heart == 0:
        print('총 점수는', score, '점입니다.')
        break

if score == 0:
    print('총 점수는', score, '점입니다.')
    print('더 열심히 공부하세요!')
elif score == 1 or score == 2 :
    print('총 점수는', score, '점입니다.')
    print('아쉽네요!')
elif score == 3:
    print('총 점수는', score, '점입니다.')
    print('만점입니다!')

print('---영단어 퀴즈를 종료합니다. 수고하셨습니다.---')