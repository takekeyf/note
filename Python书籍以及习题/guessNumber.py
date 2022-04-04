import random
randomNumber = random.randint(1,100)
while True:
    try:
        guessNumber = int(input('请输入你所猜的数字：'))
    except ValueError:
        print('错误,输入的不是数字')
    else:
        if guessNumber == randomNumber:
            print('猜对了')
            break
        elif guessNumber > randomNumber:
            print('猜大了')
        else:
            print('猜小了')

print('游戏结束。')

