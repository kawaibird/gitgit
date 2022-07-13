# Singleton pattern example

class Singleton:
    def __init__(self):
        self.inner_var = 0
        self.inner_list = []

    def input(self, x):
        assert type(x) == int, "Singleton class only can support integer."
        self.inner_var = x
        self.inner_list.append(x)


if __name__ == '__main__':
    singleton = Singleton()
    a = singleton
    b = singleton

    a.input(3)
    print(b.inner_var)
    b.input(-3)
    print(a.inner_var)
    print(a.inner_list)
    print(b.inner_list)
    a.input(0.1)
