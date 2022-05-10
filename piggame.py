import random
import time

turn = 0

my_point = 0
com_point = 0

while com_point < 100 and my_point < 100:
    if turn % 2 == 0:
        my_turn_point = 0
        while True:
            print(f'현재 총 당신의 점수는{my_point}이에요!')
            mine = input('Roll or Stop')
            if mine == 'Roll':
                num = random.randint(1,6)
                print(f'당신의 숫자는 {num}!!')
                if num == 1:
                    my_turn_point = 0
                    print('저런....1이나왓네요...0점!!')
                    print(f'현재 총 당신의 점수는{my_point}이에요!')
                    turn += 1
                    break
                else:
                    my_turn_point = my_turn_point + num
                    print(f'오호 {my_turn_point}만큼 모였어요!!')
            elif mine == 'Stop':
                my_point = my_point + my_turn_point
                print(f'당신의 총 점수는 {my_point}입니다!!')
                if my_point >= 100:
                    print('축하합니다. 승리하셨습니다!')
                    break
                else:
                    turn += 1
                    break

    else:
        com_turn_point = 0
        print('컴퓨터는 Roll할거에요!!')
        time.sleep(1)
        num_c = random.randint(1,6)
        print(f'컴퓨터의 숫자는 {num_c}입니다!')
        time.sleep(1)
        if num_c == 1:
                com_turn_point = 0
                print(f'컴퓨터 빵점....ㅠㅠ')
                time.sleep(1)
                turn += 1
        else:
            com_turn_point = com_turn_point + num_c
            print(f'컴퓨터가 모은 점수는 {com_turn_point}이에요!!')
            time.sleep(1)
            while True:
                print(f'컴퓨터의 현재 총 점수는 {com_point}에요!!')
                time.sleep(1)
                com = random.randint(1,2)
                if com == 1:
                    print('컴퓨터는 Roll할거에요!!')
                    time.sleep(1)
                    num_cc = random.randint(1,6)
                    print(f'컴퓨터의 숫자는 {num_cc}!!')
                    time.sleep(1)
                    if num_cc == 1:
                        com_turn_point = 0
                        print(f'컴퓨터 빵점....ㅠㅠ')
                        time.sleep(1)
                        print(f'컴퓨터의 현재 총 점수는 {com_point}이에요!!')
                        time.sleep(1)
                        turn += 1
                        break
                    else:
                        com_turn_point = com_turn_point + num_cc
                        print(f'컴퓨터가 {com_turn_point}만큼 모았어요!!')
                        time.sleep(1)
                else:
                    print('컴퓨터는 Stop할거에요!!!')
                    time.sleep(1)
                    com_point = com_point + com_turn_point
                    print(f'컴퓨터의 총 점수는 {com_point}입니다!!')
                    time.sleep(1)
                    if com_point >= 100:
                            print('당신은 패배하였습니다....')
                            break
                    else:
                        turn += 1
                        break
           

