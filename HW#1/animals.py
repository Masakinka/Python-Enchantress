"""
This is a class hierarchy of animals.
"""


# classes of vertebrates
class Animal:
    def __init__(self, class_name, habitat):
        self.class_name = class_name
        self.habitat = habitat

    def info(self):
        print(f'In total, there are 5 classes of vertebrates. It is a {self.class_name}.')
        print(f'My habitat is" {self.habitat}.')


class Wild(Animal):
    def __init__(self, class_name, habitat, nutrition, height):
        super().__init__(class_name, habitat)
        self.nutrition = nutrition
        self.height = height

    def size(self):
        if self.height < 10:
            print("Small")
        else:
            print("Big")


class Pet(Animal):
    def __init__(self, class_name, habitat, nickname, age):
        super().__init__(class_name, habitat)
        self.nickname = nickname
        self.age = age

    def info(self):
        print(f'It is a {self.class_name}.')
        print(f'I Live in {self.habitat}.')
        print(f'My nickname is {self.nickname}.')
        print("Age:" + self.age)


class Elephant(Wild, Pet):
    def __init__(self, class_name, habitat, nutrition, height, nickname, age):
        super().__init__(self, class_name, habitat, nutrition, height, nickname, age)
        pass


class Cat(Pet):
    def __init__(self, class_name, habitat, nickname, age):
        super().__init__(class_name, habitat, nickname, age)

    def noise(self):
        print("Says: Mew!")


class Dog(Pet):
    def __init__(self, class_name, habitat, nickname, age):
        super().__init__(class_name, habitat, nickname, age)

    def noise(self):
        print("Says: Woof!")

    def prise(self):
        print(f'{self.nickname} is good boy!')


if __name__ == "__main__":
    lion = Wild('Mammals', 'Africa', 'predator', 8)
    dog = Dog('Mammals', 'home', 'Kos', 1)
    cat = Cat('Mammals', 'home', 'Onyx', '5')
    print(lion.size())
    print(lion.info())
    print(dog.info())
    print(cat.info())
