

# 5.Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.


with open('to_sum_numbers.txt', 'w', encoding='utf-8') as write_f:
    users_number = input('Введите числа через прбел ')
    write_f.write(users_number)

with open('to_sum_numbers.txt', encoding='utf-8') as read_f:
    content = read_f.read()
    content = content.split(' ')
    content_int = []
    for i in content:
        i = int(i)
        content_int.append(i)
    result = sum(content_int)
print(result)
