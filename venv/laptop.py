"""
This is composition.
"""


class Screen:
    def __init__(self, x, y):
        self.diagonal = x * y

    def get_diagonal(self):
        return self.diagonal


class Laptop:
    def __init__(self, maker, model, x, y):
        self.maker = maker
        self.model = model
        self.diagonal = Screen(x, y)

    def get_specifications(self):
        return "%s made by %s" % (self.model, self.maker) + " with diagonal " + str(self.diagonal.get_diagonal())


if __name__ == "__main__":
    my_laptop = Laptop("Lenovo", "B460", 23, 31)
    print(my_laptop.get_specifications())
