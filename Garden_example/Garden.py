from abc import ABC, abstractmethod

# list of enums for Vegetables and Fruits
VEGETABLES = ['red_tomato']
FRUITS = ['golden']


# meta class for Singleton of Garden class
class GargenMetaClass(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


# The main garden class based on MetaClass
class Garden(metaclass=GargenMetaClass):
    def __init__(self, vegetables, fruits):
        self.vegetables = vegetables
        self.fruits = fruits

    # Show all the plants that we have in our garden
    def show_the_garden(self):
        print('I have such vegetables:')
        [print(vegetable.plant_type) for vegetable in self.vegetables]
        print('I have such fruits:')
        [print(fruit.plant_type) for fruit in self.fruits]


class Vegetables(ABC):
    def __init__(self, vegetable_type):
        self.plant_type = vegetable_type

    # states of maturity
    states = {0: 'None', 1: 'flowering', 2: 'green', 3: 'red'}

    # getter of plant type
    @property
    def plant_type(self):
        return self._plant_type

    # setter of plant type to verify if we use correct plant in our garden
    @plant_type.setter
    def plant_type(self, plant_type):
        if plant_type.lower() in VEGETABLES:
            self._plant_type = plant_type
        else:
            raise Exception(f'There is no such vegetable in the list. Your vegetable: {plant_type}')

    @abstractmethod
    def grow(self):
        raise NotImplementedError('You missed me.')

    @abstractmethod
    def is_ripe(self):
        raise NotImplementedError('You missed me.')


class Fruits(ABC):
    def __init__(self, fruit_type):
        self.plant_type = fruit_type

    # states of maturity
    states = {0: 'None', 1: 'flowering', 2: 'almost_ripe', 3: 'ripe'}

    # getter of plant type
    @property
    def plant_type(self):
        return self._plant_type

    # setter of plant type to verify if we use correct plant in our garden
    @plant_type.setter
    def plant_type(self, plant_type):
        if plant_type.lower() in FRUITS:
            self._plant_type = plant_type
        else:
            raise Exception(f'There is no such fruits in the list. Your vegetable: {plant_type}')

    @abstractmethod
    def grow(self):
        raise NotImplementedError('You missed me.')

    @abstractmethod
    def is_ripe(self):

        raise NotImplementedError('You missed me.')


class Tomato(Vegetables):
    def __init__(self, index, vegetable_type):
        super(Tomato, self).__init__(vegetable_type)
        self.index = index
        self.state = 0
        self.vegetable_type = vegetable_type

    def grow(self):
        self._change_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    # change the state of our tomato
    def _change_state(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    # print the state of our tomato
    def print_state(self):
        print(f'{self.vegetable_type} {self.index} is {Tomato.states[self.state]}')


class Apple(Fruits):
    def __init__(self, index, fruit_type):
        super(Apple, self).__init__(fruit_type)
        self.index = index
        self.state = 0
        self.fruit_type = fruit_type

    def grow(self):
        self._change_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    # change the state of our apple
    def _change_state(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    # print the state of our apple
    def print_state(self):
        print(f'{self.fruit_type} {self.index} is {Apple.states[self.state]}')


class TomatoBush():
    def __init__(self, num):
        """
        creating the list of Tomato instances in range that defined by num
        :param num: integer
        """
        self.tomatoes = [Tomato(index, 'Red_tomato') for index in range(0, num - 1)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        """
        True if all the states in the list return True. If at least one of the state return False all return False
        """
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []


class AppleTree():
    def __init__(self, num):
        """
        creating the list of Tomato instances in range that defined by num
        :param num: integer
        """
        self.apples = [Apple(index, 'Golden') for index in range(0, num - 1)]

    def grow_all(self):
        for apple in self.apples:
            apple.grow()

    def all_are_ripe(self):
        """
        True if all the states in the list return True. If at least one of the state return False all return False
        """
        return all([apple.is_ripe() for apple in self.apples])

    def give_away_all(self):
        self.apples = []


class Gardener:
    def __init__(self, name, plants):
        self.name = name
        self.plants = plants

    def harvest(self):
        print('Gardener is harvesting...')
        for plant in self.plants:
            if plant.all_are_ripe():
                plant.give_away_all()
                print('Harvesting is finished')
            else:
                print('Too early! Your plant is not ripe.')

    def handling(self):
        print('Gardener is working...')
        for plant in self.plants:
            plant.grow_all()
        print('Gardener finished')

    def check_states(self):
        for all_plants in self.plants:
            for plant in all_plants:
                if plant.state == 3:
                    return True
                return False


if __name__ == '__main__':
    # Creating list of instances for vegetables and fruits
    tomato_bush = TomatoBush(4)
    apple_tree = AppleTree(3)
    # creating only one garden instance with vegetables and fruits
    garden = Garden(vegetables=tomato_bush.tomatoes, fruits=apple_tree.apples)
    garden.show_the_garden()
    # creating the gardener instances
    gardener = Gardener('Robert', [tomato_bush, apple_tree])
    state = gardener.check_states()
    # if not state:
    #     gardener.handling()
    for i in range(3):
        gardener.handling()
    gardener.harvest()
    t = tomato_bush.tomatoes
    a = apple_tree.apples
    [print(tomato.plant_type) for tomato in tomato_bush.tomatoes]
    [print(apple.plant_type) for apple in apple_tree.apples]