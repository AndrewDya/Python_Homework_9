"""
Реализовать метакласс, позволяющий создавать всегда один и тот же объект класса
"""


class SameMeta(type):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "__instance__"):
            cls.__instance__ = super().__call__(*args, **kwargs)
        return cls.__instance__


class MyClass(metaclass=SameMeta):
    def __init__(self, name):
        self.name = name


var_1 = MyClass("What do you want")
var_2 = MyClass("Bob")

print(var_1.name)
print(var_2.name)
print(var_1 is var_2)  # True
