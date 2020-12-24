"""
This is metaclass.
"""


class Meta(type):
    def __new__(mcs, class_name, superclasses, attributes):
        print("class_name: ", class_name)
        print("superclasses: ", superclasses)
        print("attribute: ", attributes)
        return type.__new__(mcs, class_name, superclasses, attributes)


class CallMeta(Meta):
    pass


class Test(metaclass=CallMeta):
    pass


class Test1(Test, metaclass=CallMeta):
    pass


class Vi(Test1):
    def __init__(self, x):
        self.x = x


if __name__ == "__main__":
    a = Vi(7)
    print(a)
