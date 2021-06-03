
# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32


with open('salary.txt', 'r', encoding='utf-8') as f:
    my_dict = {}
    content = f.readlines()
    content = [line.rstrip() for line in content]
    for i in content:
        my_list = i.split(' ')
        my_dict[my_list[0]] = my_list[1]

    sum_salary = 0
    workers_count = 0
    for key, val in my_dict.items():
        sum_salary += float(val)
        workers_count += 1
    print(f'Количество сотрудников - {workers_count} человек')
    print(f'Фонд заработной платы - {sum_salary} рублей')
    print(f'Средняя заработная плата - {sum_salary/workers_count} рублей')
    print()
    print('Сотрудники с зарплатой меньше 20 000 рублей:')
    for key, val in my_dict.items():
        if float(val) < 20000:
            print('    ', key)




