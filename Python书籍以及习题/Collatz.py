def collatz(number):
        if number % 2 == 0:
            return number // 2 
        else:
            return number*3 + 1

while True:
    try:
        num = int(input('enter your number:'))
    except ValueError:
        print('ValuesError:please enter an integer')
        continue
    else:
        if num == 0:
            print('ValuesError:the number 0 cannot be considered divisor')
            continue 
        else:
            while num != 1:
                num = collatz(num)
                print(num)
            break



