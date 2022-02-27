class Car:
    is_police: bool = False

    def __init__(self, speed: int, color: str, name: str):
        """
        Конструктор класса
        :param speed: текущая скорость автомобиля
        :param color: цвет автомобиля
        :param name: название марки автомобиля
        """
        self.speed = speed
        self.color = color
        self.name = name

        # pass  # опишите конструктор

    def go(self) -> None:
        """
        Увеличивает значение скорости на 15
        :return: в stdout сообщение по формату
            'Машина <название марки машины> повысила скорость на 15: <текущая скорость машины>'
        """
        self.speed = self.speed + 15
        return print(f'Машина {self.name} повысила скорость на 15: {self.speed}')
        # pass  # Ваш код здесь

    def stop(self) -> None:
        """
        При вызове метода скорость становится равной '0'
        :return: в stdout сообщение по формату '<название марки машины>: остановилась'
        """
        # pass  # Ваш код здесь
        self.speed = 0
        return print(f'{self.name}: остановилась')

    def turn(self, direction: str) -> None:
        """
        Принимает направление движения автомобиля
        :param direction: строковое представление направления движения, может принимать только
            следующие значения: 'направо', 'налево', 'прямо', 'назад'
        :return: в stdout сообщение по формату
            '<название марки машины>: движется <direction>'
        """
        # pass  # Ваш код здесь
        return print(f'{name}: движется {direction}')

    def show_speed(self) -> None:
        """
        Проверка текущей скорости автомобиля
        :return: в stdout выводит сообщение формата
            '<название марки машины>: текущая скорость <значение текущей скорости> км/час'
        """
        if self.is_police is True:
            return print('Вруби мигалку и забудь про скорость!')
        else:
            return print(f'{self.name}:текущая скорость {self.speed} км/час')
        # pass  # Ваш код здесь


class TownCar(Car):
    def show_speed(self) -> None:
        if self.speed > 60:
            return print('Alarm!!! Speed!!!')
        else:
            return print(f'{self.name}:текущая скорость {self.speed} км/час')


class WorkCar(Car):
    def show_speed(self) -> None:
        if self.speed > 40:
            return print('Alarm!!! Speed!!!')
        else:
            return print(f'{self.name}:текущая скорость {self.speed} км/час')


class SportCar(Car):

    def turn(self, direction: str) -> None:
        directions = ['направо', 'налево', 'прямо', 'назад']
        if direction in directions:
            return print(f'{self.name}({self.__class__.__name__}): движется {direction}')
        else:
            raise ValueError(f'нераспознанное направление движения:{direction}')
class PoliceCar(Car):
    is_police: bool = True

    def show_speed(self) -> None:

        if self.is_police is True:
            return print(f'{self.name}:текущая скорость {self.speed} км/час.\nВруби мигалку и забудь про скорость!')



# определите классы TownCar, WorkCar, SportCar, PoliceCar согласно условия задания


if __name__ == '__main__':
    town_car = TownCar(41, "red", 'WW_Golf')
    work_car = WorkCar(41, 'yellow', 'BobCat')
    police_car = PoliceCar(120, "blue", 'BMW')
    sport_car = SportCar(300, 'white', 'Ferrari')
    town_car.go()  # Машина WW_Golf повысила скорость на 15: 56
    town_car.show_speed()  # WW_Golf: текущая скорость 56 км/час
    work_car.show_speed()  # Alarm!!! Speed!!!
    town_car.stop()  # WW_Golf: остановилась
    police_car.show_speed()
    # # BMW: текущая скорость 120 км/час
    # # Вруби мигалку и забудь про скорость!
    sport_car.turn('назад')  # Ferrari(SportCar): движется назад
    # sport_car.turn('right')
    # """
    # Traceback (most recent call last):
    #   ...
    # ValueError: нераспознанное направление движения
    # """
