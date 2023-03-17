"""
Задание 3.

Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).

П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку str
str(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
"""
class Worker:
    name: str
    surname: str
    position: str
    income_list = {30000: 5000, 40000: 7000, 50000: 8000,
                   60000: 9000, 70000: 10000, 80000: 11000, 100000: 15000}
    _income = income_list

    def __init__(self, name, surname, income, position) -> None:
        self.name = name
        self.surname = surname
        self.income = income
        self.position = position


class Position(Worker):

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self, income):

        return self.income_list.get(income) + income

    def __str__(self) -> str:
        return f"{self.name} {self.surname}, {self.position}: {self.income + self.income_list.get(self.income)}"


ivanov_ivan = Position("Иван", "Иванов", 100000, "программист")


print(ivanov_ivan.get_total_income(ivanov_ivan.income))
print(ivanov_ivan)