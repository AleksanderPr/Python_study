
# 2. Для списка реализовать обмен значений соседних элементов. Значениями обмениваются
# элементы с индексами 0 и 1, 2 и 3 и т. д. При нечётном количестве элементов последний
# сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию
# input().

user_nums = input('Введите элементы через "," ')
user_nums = user_nums.split(',')
print(f'Исхоный список  {user_nums}')
# для нечетного количества элементов в списке
if len(user_nums) % 2 != 0:
    for i in range(0, len(user_nums)-1, 2):
        user_nums[i], user_nums[i + 1] = user_nums[i + 1], user_nums[i]
# для четного количества элементов в списке
else:
    for i in range(0, len(user_nums), 2):
        user_nums[i], user_nums[i + 1] = user_nums[i + 1], user_nums[i]

print(f'Конечный список {user_nums}')