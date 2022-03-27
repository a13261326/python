import time


class TrafficLight:
    __color = ["\033[31m "'RED', "\033[33m "'YELLOW', "\033[32m "'GREEN']
    __secs = [4, 2, 3]
    a_dict = {key: value for key, value in zip(__color, __secs)}

    def running(self):
        for i in (self.a_dict):
            print(f'{i}   {self.a_dict[i]}  сек')
            time.sleep(self.a_dict[i])


if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()
# red 4 сек
# yellow 2 сек
# green 3 сек
