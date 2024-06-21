class Person:
    def __init__(self, name, age):
        self._name = name  # Защищенный атрибут
        self._age = age  # Защищенный атрибут

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age > 0:
            self._age = age

    # Абстрактный метод, который должен быть переопределен в наследниках
    def do_something(self):
        pass

class Student(Person):
    def do_something(self):
        print(f"{self.get_name()} is studying.")

# Пример использования
student = Student("Alex", 20)
student.do_something()
