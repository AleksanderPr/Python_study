

#4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите параметры,
# общие для приведённых типов. В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.


# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад
# и передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).


class Storage:
    equipment_list = {}


class Equipment(Storage):
    def __init__(self, name, producer, number, size, defect):
        self.name = name
        self.producer = producer
        self.number = number
        self.size = size
        self.defect = defect
        try:
            if not isinstance(number, (int, float)):
                self.number = 0
                raise ValueError
        except ValueError:
            print('Проврьте вводимые данные о количестве техники')

    def get_equipment(self):
        if self.name in Storage.equipment_list:
            Storage.equipment_list[self.name] += self.number
        else:
            Storage.equipment_list[self.name] = self.number

    # Отправка техники в подразделение
    @classmethod
    def sent_qequipment(cls, name, number, division):
        Storage.equipment_list[name] -= number
        print(f'{number} {name} отправлены в {division}')



    def get_info(self):
        print(f'name: {self.name}, producer: {self.producer}, number: {self.number}, size: {self.size},defect: {self.defect}')


class Printers(Equipment):
    def __init__(self, name, producer, number, size, defect, coloured, network):
        super().__init__(name, producer, number, size, defect)
        self.coloured = coloured
        self.network = network


    def get_info(self):
        Equipment.get_info(self)
        print(f' coloured: {self.coloured}, network: {self.network}')


class Scaners(Equipment):
    def __init__(self, name, producer, number, size, defect, scan_type, paper_format):
        super().__init__(name, producer, number, size, defect)
        self.scan_type = scan_type
        self.paper_format = paper_format

    def get_info(self):
        Equipment.get_info(self)
        print(f' scan_type: {self.scan_type}, paper_format: {self.paper_format}')


class Copiers(Equipment):
    def __init__(self, name, producer, number, size, defect, printing_tech, paper_format):
        super().__init__(name, producer, number, size, defect)
        self.printing_tech = printing_tech
        self.paper_format = paper_format

# Поступила партия принтеров
printer1 = Printers(name='printer1', producer='Sony', number=4, size=2, defect=False, coloured=True, network=True)
printer1.get_equipment()

# Поступила партия таких же принтеров
printer1 = Printers(name='printer1', producer='Sony', number=6, size=2, defect=False, coloured=True, network=True)
printer1.get_equipment()

# Поступила партия сканеров
scaner1 = Scaners(name='scaner1', producer='Panasonic', number=7, size=2, defect=False, scan_type='tablet', paper_format='A3')
scaner1.get_equipment()

# Количество техники на складе до отправки
print(f'На складе в настоящий момент:  {Storage.equipment_list}')
print()

# отправка техники в подразделение
Equipment.sent_qequipment(name='printer1', number=2, division='1 отдел')
print()

# Количество техники на складе после отправки
print(f'На складе в настоящий момент:  {Storage.equipment_list}')
print()
print('Информация о технике')
print(printer1.get_info())
print(scaner1.get_info())
