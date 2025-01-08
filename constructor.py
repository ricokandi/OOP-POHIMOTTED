"""Constructor exercise."""


class Empty:
    """An empty class without constructor."""

    pass


class Person:
    """Represent person with firstname, lastname and age."""

    def __init__(self):
        """Constructor without parameters."""
        self.firstname = ""
        self.lastname = ""
        self.age = 0
    pass


class Student:
    """Represent student with firstname, lastname and age."""

    def __init__(self, firstname, lastname, age):
        """Constructor with parameters."""
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    pass


if __name__ == '__main__':
    # empty usage
    empty = Empty()

    # 3 x person usage
    tiina = Person("Eedu", "Peedu", 1)
    maia = Person("Markus", "Erkmann", 17)
    ago = Person("Rico", "Kandi", 16)

    # 3 x student usage
    tiina = Student("Tiina", "Kopp", 20)
    maia = Student("Maia", "Maasikas", 10)
    ago = Student("Ago", "Maier", 9)
    pass
    # 3 x student usage
    tiina = Student("Tiina", "Kopp", 20)
    maia = Student("Maia", "Maasikas", 10)
    ago = Student("Ago", "Maier", 9)
    pass
