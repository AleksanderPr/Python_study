# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

distance_1 = int(input('Введите начальную дистанцию'))
distance_2 = int(input('Введите конечную дистанцию'))
day_count = 1
while distance_1 < distance_2:
    distance_1 += distance_1 * 0.1
    day_count += 1
print(day_count)




















