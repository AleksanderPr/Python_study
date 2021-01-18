# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды
# и выведите в формате чч:мм:сс. Используйте форматирование строк



user_seconds = int(input('Введите время, в секундах '))
hour = user_seconds // 3600
minutes_result = user_seconds % 3600 // 60
minutes_float = user_seconds % 3600
seconds = minutes_float % 60
print(f"{hour:0>2d}:{minutes_result:0>2d}:{seconds:0>2d}")













