

# 6. Реализовать два небольших скрипта:
# ●	итератор, генерирующий целые числа, начиная с указанного;
# ●	итератор, повторяющий элементы некоторого списка, определённого заранее.
# Подсказка: используйте функцию count() и cycle() модуля itertools. Обратите внимание,
# что создаваемый цикл не должен быть бесконечным. Предусмотрите условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 — завершаем цикл.
# Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.

from itertools import count, cycle

count_list = []
for i in count(3):
    print(i)
    count_list.append(i)
    if i == 10:
        break

print(count_list)

check_condition = 0
for el in cycle(count_list):
    if check_condition > 15:
        break
    print(el)
    check_condition += 1
