
# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.


user_number = int(input('Введите целое положительное число '))
list = []
while user_number > 0:
    list.append(user_number % 10)
    user_number = user_number // 10

print('Самая большая цифра: ', max(list))




