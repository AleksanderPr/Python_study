
# 5. Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделённых пробелом
# и снова нажать Enter. Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел к
# полученной ранее сумме и после этого завершить программу.

# Первый вариант решения.
# Здесь, правда, программа прекращает работу не только при вводе спецсимвола, но и любого "нечисла",
# что кажется более оправдано, ведь если введено нечисло, сложение все равно не будет выполняться

def sum_in_string(string):
    global condition_check
    string = string.split(' ')
    result = 0
    for i in string:
        if i.isdigit():
            i = float(i)
            result += i
        else:
            condition_check = False
            break
    return result


condition_check = True

global_result = 0

# Не могу понять почему PyCharm здесь подчеркивает, что не так?
while condition_check == True:
    user_string_number = input('Введите числа через пробел ')
    function_result = sum_in_string(user_string_number)
    global_result += function_result
    print(global_result)


#
# Второй вариант решения.
# Прекращение работы программы только при вводе спецсимвола.
# Если вводится не число, то обрабатывется ошибка и программа продолжает выполняться

# def sum_in_string(string):
#     global condition_check
#     string = string.split(' ')
#     symbols = ".,:;!_*-+()/#%&"
#     result = 0
#     for i in string:
#         if i in symbols:
#             condition_check = False
#             break
#         else:
#             try:
#                 i = float(i)
#                 result += i
#             except ValueError:
#                 break
#
#     return result
#
#
# condition_check = True
#
# global_result = 0
# while condition_check == True:
#     user_string_number = input('Введите числа через пробел ')
#     function_result = sum_in_string(user_string_number)
#     global_result += function_result
#     print(global_result)