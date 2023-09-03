print("Hello,World!")  # 1.1

name = input('What is your name ')  # 3
print(f'Hello {name} !')

a = int(input('введите первое число '))  # 4
b = int(input('введите первое число '))
rez = a + b
print(f'Резульат равно  {rez}')

print("*********\n*            *\n*            *\n*********")  # 1.2

num = int(input('введите 4-х значное число: '))  # 1.3 test
num1 = num // 1000
num2 = (num - num1 * 1000) // 100
num3 = (num - num1 * 1000 - num2 * 100) // 10
num4 = num - num1 * 1000 - num2 * 100 - num3 * 10
print(f'Тысяч {num1} \n Соток {num2} \n Десяток {num3} \n Единиц {num4}')
