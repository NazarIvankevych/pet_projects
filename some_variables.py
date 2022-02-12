# number = 10


# def change_number():
#     global number
#     print(f"Number not change inside a function and still is: {number}.")
#     def another_change():
#         global number
#         number = 35
#         print(f"The variable 'number' is change in this function into {number}")
#     print(f"Before making change - {number}.")
#     another_change()
#     print(f"From another function the number is - {number}")

# change_number()
# print(f"Value of numbers is - {number}")


# word = "Hello there!"

# def change_text():
#     global word
#     name = "Nazar"
#     word = "I`m working well!"
#     print(f"Show changing in global variable - {word}")
#     def another_text():
#         nonlocal name
#         print(f"Before his name is - {name}")
#         name = "Olena"
#     another_text()
#     return f"Her name is - {name}"

# change_text()
# print(f"Also changing - {word}")
# print(change_text())


class Parrot:

    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class Penguin:

    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

# common interface
def flying_test(bird):
    bird.fly()
    bird.swim()

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)
