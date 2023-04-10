"""
Реализовать 2 дескриптора (провести валидацию для одного типа данных/для типа данных и ограничения числа)
"""


class StringField:
    def __set__(self, instance, value):
        if not isinstance(value, str) or not value.isalpha():
            raise ValueError(f"{self.name} должно содержать только буквы")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class AgeField:
    def __set__(self, instance, value):
        if not isinstance(value, int) or value < 18:
            raise ValueError(
                f"{self.name} должен быть целым числом и больше 18")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class Worker:
    name = StringField()
    surname = StringField()
    position = StringField()
    age = AgeField()

    def __init__(self, name, surname, position, age, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.age = age
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return sum(self._income.values())

    def __str__(self):
        return f"{self.get_full_name()}, должность: {self.position}, возраст: {self.age}, доход: {self.get_total_income()}"


name = input("Введите ваше имя: ")
age = int(input("Введите ваш возраст: "))

john_cena = Position(name, "Cena", "Manager", age, 50000, 10000)

print(john_cena)
