"""
3. Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""


class Worker:
    """Работник"""

    name = ''
    """Имя Работника"""

    surname = ''
    """Фамилия Работника"""

    position = ''
    """Должность"""

    _income_ = {"wage": 0, "bonus": 0}

    def __init__(self, name, surname, position):
        """Конструктор

        Args:
            name (str): Имя Работника
            surname (str): Фамилия Работника
            position (str): Должность
        """
        self.name = name
        self.surname = surname
        self.position = position

    def set_salary(self, wage, bonus):
        self._income_["wage"] = wage
        self._income_["bonus"] = bonus


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        """Конструктор

        Args:
            wage (int): Зарплата
            bonus (int): Оклад
        """
        Worker.__init__(self, name, surname, position)
        Worker.set_salary(self, wage, bonus)

    def get_full_name(self):
        return f'Работник: {self.name} {self.surname}.'

    def get_total_income(self):
        return f'Зарплата={self._income_["wage"]} р. Оклад={self._income_["bonus"]}р. Итого получает {int(self._income_["wage"]) + int(self._income_["bonus"])} р.'


worker_1 = Position("Игорь", "Петров", "Инженер", 50000, 23000)
print(worker_1.__dict__)
print(worker_1._income_)
print(worker_1.get_full_name())
print(worker_1.get_total_income(), end='\n')

worker_2 = Position("Александр", "Сидоров", "Программист", 60000, 27000)
print(worker_2.__dict__)
print(worker_2._income_)
print(worker_2.get_full_name())
print(worker_2.get_total_income(), end='\n')
