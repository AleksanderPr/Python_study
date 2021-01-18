# 1. Поработайте с переменными, создайте несколько, выведите на экран.
# Запросите у пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран


courses_name = 'Big data'
study_period = 18

user_name = input('Введите Ваше имя ')
user_age = int(input('Введите Ваш возраст '))
if user_age % 10 != 1:
     print(f"{user_name} начал изучать {courses_name} в возрасте {user_age} лет")
else:
    if user_age != 11:
        print(f"{user_name} начал изучать {courses_name} в {user_age} год")
    else:
        print(f"{user_name} начал изучать {courses_name} в {user_age} лет")


print('Удачи и сил в ближайшие', study_period, 'месяцев))')

