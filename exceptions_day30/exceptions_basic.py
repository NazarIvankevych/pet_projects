# # FileNotFound
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError as error_file:
#     # If not, catch exeption
#     # print(f"This file - {error_file}, not exist")
#     # Create a file
#     file = open("a_file.txt", "w")
#     file.write("Something")
# # Catch exception
# # except KeyError:
# #     print("That key is not exist")
# except KeyError as error_message:
#     print(f"The key - {error_message}, does not exist!")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed")
#     # raise errors
#     raise TypeError("This is an error that I made up!")
#
# height = float(input("Height: "))
# weight = int(input("Weight: ")),
# if height > 3:
#     raise ValueError("Human height is to big")
# bmi = weight / height ** 2
# print(bmi)


fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit Pie")
    else:
        print(fruit + " pie")


make_pie(4)