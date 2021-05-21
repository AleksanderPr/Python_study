
# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года
# относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.


# winter = [12, 1, 2]
# spring = [3, 4, 5]
# summer = [6, 7, 8]
# autumn = [9, 10, 11]

input_month = int(input('Введите номер месяца '))

# if input_month in winter:
#     print('Зима')
# elif input_month in spring:
#     print('Весна')
# elif input_month in summer:
#     print('Лето')
# elif input_month in autumn:
#     print('Осень')
# else:
#     print('Нужно было ввести число от 1 до 12')

dict_year = {
    12: 'Зима',
    1: 'Зима',
    2: 'Зима',
    3: 'Весна',
    4: 'Весна',
    5: 'Весна',
    6: 'Лето',
    7: 'Лето',
    8: 'Лето',
    9: 'Осень',
    10: 'Осень',
    11: 'Осень'
}

print(dict_year.get(input_month))
if dict_year.get(input_month) == None:
    print('Нужно было ввести число от 1 до 12')
