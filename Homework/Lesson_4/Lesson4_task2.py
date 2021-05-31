

# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для его формирования используйте генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].


origin_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
resuls_list = [origin_list[i] for i in range(1, len(origin_list)) if origin_list[i] > origin_list[i-1]]
print(resuls_list)