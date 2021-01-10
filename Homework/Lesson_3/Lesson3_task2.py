

# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры
# как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.


def person(name, surname, birthday_year, town, mail, phone):
    print(name, surname, birthday_year, town, mail, phone)

def person2(**kwargs):
    result = []
    for val in kwargs.values():
        val = str(val)
        result.append(val)
    string = ' '.join(result)
    print(string)


person(name='Alex', surname='Ivanov', birthday_year=1985, town='Moscow', mail='Alex@mail.ru', phone=8926123432)


person2(name='Alex', surname='Ivanov', birthday_year=1985, town='Moscow', mail='Alex@mail.ru', phone=8926123432)