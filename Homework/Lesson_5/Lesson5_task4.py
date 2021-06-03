

# 4.	Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

russian_dict = {
    1: 'Один',
    2: 'Два',
    3: 'Три',
    4: 'Четыре'
}

english_dict = {}
numbers = []
with open('numbers.txt', encoding='utf-8') as f:
    content = f.readlines()
    for i in content:
        text_number, number = i.split('—')
        number = number.strip()
        numbers.append(number)
        english_dict[number] = text_number


with open('numbers_translate.txt', 'w', encoding='utf-8') as f_translate:
    for i in numbers:
        result_translate = russian_dict[int(i)]
        f_translate.writelines(f'{result_translate} - {i}\n')


