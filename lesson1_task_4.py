# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.

user_number = int(input('Введите целое положительное число '))
max_num = user_number % 10  # Узнать последнюю цифру и предположить, что она самая большая
user_number = user_number // 10  # Отбросить последнюю цифру
while user_number > 0:
    if max_num < user_number % 10:
        max_num = user_number % 10
    user_number = user_number // 10
print('Самая большая цифра: ', max_num)
