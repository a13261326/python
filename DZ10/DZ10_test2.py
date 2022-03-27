from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, num: float):
        self.num = num

    @property
    @abstractmethod
    def calculate(self):
        pass


class Coat(Clothes):
    @property
    def calculate(self):
        return round(self.num / 6.5 + 0.5, 2)


class Costume(Clothes):
    @property
    def calculate(self):
        return round(2 * self.num + 0.3, 2)


if __name__ == '__main__':
    coat = Coat(45.0)
    costume = Costume(3)
    print(coat.calculate)  # 7.42
    print(costume.calculate)  # 6.3
    total_consumption = round(costume.calculate + coat.calculate,2)
    print(total_consumption)  #13.72
