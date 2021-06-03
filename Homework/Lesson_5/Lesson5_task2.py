
# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.



with open('text44.txt', 'r') as f:
    lines = f.readlines()
    num_lines = len([l for l in lines if len(l) > 1])
    print('Количество непустых строк: ', num_lines)
    for line_number, line in enumerate(lines, 1):
        print(f'В строке №{line_number} - {len(line.split())} слов')

