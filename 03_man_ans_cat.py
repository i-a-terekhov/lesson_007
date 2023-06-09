import random
from random import randint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.


class Street:

    def __init__(self):
        self.name = 'Улица'
        self.dirty = 1000
        self.food_for_cat = 0
        # self.is_cat_here = True

    def __str__(self):
        return 'Это суровая улица'


class House:

    def __init__(self, name='Умолчательное название'):
        self.name = name
        self.food = 0
        self.food_for_cat = 150
        self.dirty = 0
        self.money = 0

    def __str__(self):
        return 'Статус дома. Название {}: еда - {}, еда для кошек - {}, грязь - {}, деньги - {}'.format(
            self.name, self.food, self.food_for_cat, self.dirty, self.money)


class Cat:

    def __init__(self, name):
        self.name = name
        self.home = Street()
        self.satiety = 30  # сытость
        self.drowsiness = 30  # сонливость
        self.happiness = 0

    def __str__(self):
        return 'Статус котика. Имя {} живет в/на {}: сытость {}, сонливость {}, счастье {}'.format(
            self.name, self.home.name, self.satiety, self.drowsiness, self.happiness)

    def at_home(self):
        if type(self.home) is House:
            return True
        else:
            print('Кот {} еще живет на улице'.format(self.name))
            return False

    def there_is_enough_food(self):
        print('Кот проверяет количество корма в доме {} - {}'.format(self.home.name, self.home.food_for_cat), end='')
        if self.home.food_for_cat >= 50:
            print(' - корма хватает, котик кушает')
            return True
        else:
            print(' - корма недостаточно :(')
            return False

    def make_a_mess(self):  # устроить беспорядок
        if self.at_home:
            self.drowsiness += 20
            self.home.dirty += 20

    def eat(self):
        if self.at_home() and self.there_is_enough_food():
            self.home.food_for_cat -= 50
            self.satiety += 80 + int(random.random() * 20)
            self.drowsiness += 30

    def sleep(self):
        self.drowsiness -= 100

    def is_dead(self):
        if self.satiety <= 0:
            print('Кот {} умер с голоду'.format(self.name))
            return True
        else:
            return False

    def act(self):
        self.satiety -= 20
        if self.satiety <= 50:
            print('Кот {} решил покушать, так как его сытость составляет {}'.format(self.name, self.satiety))
            self.eat()
        elif self.drowsiness >= 100:
            print('Кот {} решил поспать'.format(self.name))
            self.sleep()
        else:
            print('Кот {} решил устроить беспорядок'.format(self.name))
            self.make_a_mess()


class Man:

    def __init__(self, home_name):
        self.name = 'Челик'
        self.home = House(name=home_name)
        self.satiety = 80  # сытость
        self.drowsiness = 30  # сонливость
        self.happiness = 0

    def __str__(self):
        return 'Статус хозяина. Сытость {}, сонливость {}, счастье {}'.format(
            self.satiety, self.drowsiness, self.happiness)

    def bring_cat_into_the_house(self, CatExem):
        if isinstance(CatExem, Cat):
            if not CatExem.at_home():
                print('Кота нашли на улице и отнесли в дом {}'.format(self.home.name))
                CatExem.home = self.home

    def is_dead(self):
        if self.satiety <= 0:
            print('Хозяеин {} умер с голоду'.format(self.name))
            return True
        else:
            return False

    def there_is_enough_food(self):
        print('Хозяин проверяет количество еды в доме {} - {}'.format(self.home.name, self.home.food), end='')
        if self.home.food >= 50:
            print(' - еды хватает, человек кушает')
            return True
        else:
            print(' - еды недостаточно :(')
            return False

    def eat(self):
        if self.there_is_enough_food():
            self.home.food_for_cat -= 50
            self.satiety += 80
            self.drowsiness += 30

    def sleep(self):
        self.drowsiness -= 100

    def work(self):
        self.home.money += 150

    def bye_food_for_cat(self):
        self.home.money -= 50
        self.home.food_for_cat += 100

    def bye_food(self):
        self.home.money -= 50
        self.home.food += 100

    def act(self):
        self.satiety -= 20
        if self.satiety <= 50:
            print('Хозяин {} решил покушать, так как его сытость составляет {}'.format(self.name, self.satiety))
            self.eat()
        elif self.drowsiness >= 100:
            print('Хозяин {} решил поспать'.format(self.name))
            self.sleep()
        elif self.home.food_for_cat <= 100:
            print('Хозяин {} решил купить еды котику'.format(self.name))
            self.bye_food_for_cat()
        elif self.home.food <= 100:
            print('Хозяин {} решил купить еду себе'.format(self.name))
            self.bye_food()
        else:
            print('Хозяин {} решил сходить на работу'.format(self.name))
            self.work()


Chelik = Man('Домик')
Bubble = Cat('Бублик')
Baton = Cat('Батон')

for i in range(100):
    print('--------------------------------- день {} ----------------'.format(i))
    if isinstance(Bubble, Cat):
        Bubble.act()
        if Bubble.is_dead():
            Bubble = None
        else:
            print(Bubble)
    if isinstance(Baton, Cat):
        Baton.act()
        if Baton.is_dead():
            Baton = None
        else:
            print(Baton)
    if isinstance(Chelik, Man):
        Chelik.act()
        if Chelik.is_dead():
            Chelik = None
        else:
            print(Chelik)
    if Chelik is not None:
        Chelik.bring_cat_into_the_house(Bubble)
        Chelik.bring_cat_into_the_house(Baton)
        print(Chelik.home)
    else:
        print('Человек умер, дом запустел')


# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
