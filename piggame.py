turn = random.randrange(0, 2)

my_point = 0
com_point = 0

while True:
    if turn % 2 == 0:
        my_turn_point = 0
        while True:
            mine = input('Roll or Stop')
            if mine == 'Roll':
                num = random.randint(1,6)
                print(f'당신의 숫자는 {num}!!')
                if num == 1:
                    my_turn_point = 0
                    print('저런....1이나왓네요...0점!!')
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
        com_turn_point = 0
        while True:
            num_c = random.randint(1,6)
            print(f'컴퓨터의 숫자는 {num_c}입니다!')
            if num_c == 1:
                    com_turn_point = 0
                    print(f'컴퓨터 빵점....ㅠㅠ')
                    break
            else:
                com_turn_point = com_turn_point + num_c
                print(f'컴퓨터가 모은 점수는 {com_turn_point}이에요!!')
                while True:
                    com = random.randint(1,2)
                    if com == 1:
                        print('컴퓨터는 Roll할거에요!!')
                        num_cc = random.randint(1,6)
                        print(f'컴퓨터의 숫자는 {num_cc}!!')
                        if num_cc == 1:
                            com_turn_point = 0
                            print(f'컴퓨터 빵점....ㅠㅠ')
                            break
                        else:
                            com_turn_point = com_turn_point + num_cc
                            print(f' {my_turn_point}만큼 모였어요!!')
                    else:
                        com_point = com_point + com_turn_point
                        print(f'컴퓨터의 총 점수는 {com_point}입니다!!')
                        if com_point >= 100:
                             print('당신은 패배하였습니다....')
                             break
           
    turn += 1
