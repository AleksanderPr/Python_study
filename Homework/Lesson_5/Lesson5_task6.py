
# 6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и
# наличие лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
# Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
#                                         Физика:   30(л)   —   10(лаб)
#                                         Физкультура:   —   30(пр)   —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

my_dict = {}
with open('lessons.txt', encoding='utf-8') as read_f:
    content = read_f.readlines()
    for i in content:
        i = i.strip()
        lesson_name, lesson_hours = i.split(':')
        lesson_hours = lesson_hours.replace("(л)", "", 1)
        lesson_hours = lesson_hours.replace("(пр)", "", 1)
        lesson_hours = lesson_hours.replace("(лаб)", "", 1)
        my_dict[lesson_name] = lesson_hours


for key, val in my_dict.items():
    split_val = val.split(' ')
    sum_of_hours = 0
    for i in split_val:
        try:
            i = int(i)
            sum_of_hours += i
        except ValueError:
            pass
    my_dict[key] = sum_of_hours

print(my_dict)
