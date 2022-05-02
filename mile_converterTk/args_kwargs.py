<<<<<<< HEAD
# from random import *
#
#
# def add(*args):
#     for x in args:
#         x += x
#         print(x * args)
#
#
# add(randint(1, 20))

# def canculate(**kwargs):
#     print(kwargs)
#
#
# canculate(add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]

    def looping_dict(self):
        for k in self.make:
            return k
        for k in self.model:
            return k

my_car = Car(make="Toyota", model='RAV4')
print(f"In future, I want to buy - {my_car.make}")
print(f"And it`s model is - {my_car.model}")
=======
# from random import *
#
#
# def add(*args):
#     for x in args:
#         x += x
#         print(x * args)
#
#
# add(randint(1, 20))

# def canculate(**kwargs):
#     print(kwargs)
#
#
# canculate(add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]

    def looping_dict(self):
        for k in self.make:
            return k
        for k in self.model:
            return k

my_car = Car(make="Toyota", model='RAV4')
print(f"In future, I want to buy - {my_car.make}")
print(f"And it`s model is - {my_car.model}")
>>>>>>> 6bb0f90e7b2042da98278b61b14da243c44df510
print(f"Some loops in two dict:\n{my_car.looping_dict()}")