from random import randint
#3扇門機率問題
win = 0
lose = 0
for i in range(1,10001):
    #一開始的門
    com = randint(0, 2)
    list01 = ['羊','羊']
    list01.insert(com, '車')
    print('一開始的門:', list01)

    #玩家選擇的門
    player_choice = randint(0, 2)
    print('玩家選擇:', list01[player_choice])

    #被選擇後剩餘的門
    del list01[player_choice]
    print('剩餘的門:', list01)

    #主持人幫門開掉一扇有羊的門
    list01.remove('羊')
    print('最後的門:', list01)

    if list01[0] == '車':
        print('恭喜玩家獲得汽車!!')
        win += 1
    else:
        print('可惜沒獲得汽車!!')
        lose += 1
total = win + lose
print('贏的機率:', win / total * 100,'%')
print('輸的機率:', lose / total * 100,'%')