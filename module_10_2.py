from threading import Thread
import threading
import time



class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()          # переопределение метода init
        self.name = str(name)       # имя рыцаря
        self.power = int(power)     # сила рыцаря
        self.counter = 100          # количество воинов
        self.days = 0               # кол-во дней, изначально составляет 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.counter > 0:
            self.counter -=self.power
            self.days += 1
            print(f'{self.name} сражается {self.days} день(дня), осталось {self.counter} воинов."')
            time.sleep(1) # прошествие 1 дня сражения (1 секунды)
        print(f'{self.name} одержал победу спустя {self.days} дней(дня)')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()


print("Все битвы закончились!")


