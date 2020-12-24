"""
This is aggregation.
"""


class StringQuantity:
    def __init__(self, string):
        self.string = string

    def get_string(self):
        return self.string


class Guitare:
    def __init__(self, maker, model, string):
        self.maker = maker
        self.model = model
        self.string = string

    def print_message(self):
        print(f'This is model {self.model} made by {self.maker} with {self.string.get_string()} string.')


if __name__ == "__main__":
    count = StringQuantity(6)
    Yamaha = Guitare("Yamaha", "F 310", count)
    Yamaha.print_message()

