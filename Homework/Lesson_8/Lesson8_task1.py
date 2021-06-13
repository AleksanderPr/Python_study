

# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:
    data_atribute = []
    data_list = []

    def __init__(self, data):
        self.data = data
        Data.data_atribute.append(self.data)

    @classmethod
    def get_int_data(cls):
        for i in cls.data_atribute:
            data_dict = {}
            day, month, year = i.split('.')
            data_dict['day'] = int(day)
            data_dict['month'] = int(month)
            data_dict['year'] = int(year)
            Data.data_list.append(data_dict)

    @staticmethod
    def get_validation_check(data_list):
        for data in data_list:
            if data['day'] > 31 or data['day'] < 1:
                print('Неправильно указан день в дате', data)
            if data['month'] > 12 or data['month'] < 1:
                print('Неправильно указан месяц в дате', data)
            if data['year'] > 2040 or data['year'] < 1950:
                print('Неправильно указан год в дате', data)


d1 = Data('01.05.1985')
d2 = Data('15.05.2015')
d3 = Data('22.05.2017')
d4 = Data('32.05.2017')
Data.get_int_data()
for i in Data.data_list:
    print(i)
Data.get_validation_check(data_list=Data.data_list)