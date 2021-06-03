
# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать
# данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
import json

total_list = []
with open('firms.txt', encoding='utf-8') as f:
    content = f.readlines()
    total_profit = 0
    profit_firms = 0
    firm_dict = {}
    average_profit_dict = {}

    for i in content:
        name, form, revenue, costs = i.split()
        profit = int(revenue) - int(costs)
        firm_dict[name] = profit
        if profit > 0:
            profit_firms += 1
            total_profit += profit
    average_profit = total_profit / profit_firms
    average_profit_dict['average_profit'] = average_profit
    total_list.append(firm_dict)
    total_list.append(average_profit_dict)

with open('firms.json', 'w', encoding='utf-8') as f_json:
    json_firms = json.dump(total_list, f_json)

print(total_list)