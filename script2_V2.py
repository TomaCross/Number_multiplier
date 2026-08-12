
print('---Умножатель чисел!---')
while True:
    user = False
    try:
        num1 = int(input('ведите первое число='))
    except ValueError:
        print('Пожалуйста введите цифру!')
        continue
    try:
        num2 = int(input('ведите второе число='))
    except ValueError:
        print('Пожалуйста введите цифру!')
        continue
    try:
        num3 = int(input('ведите третье число='))
    except ValueError:
        print('Пожалуйста введите цифру!')
        continue
    try:
        num4 = int(input('ведите шетыре число='))
    except ValueError:
        print('Пожалуйста введите цифру!')
        continue
    print(num1 * num2 * num3 * num4)
