# !todo: Need to count all squirrels with different colors
import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
colors = data["Primary Fur Color"]
# print(type(colors))
# add all colors from csv into list with loops and conditions
# list_colors = colors.to_list()
# print(list_colors)
# gray = []
# black = []
# cinnamon = []
# for color in list_colors:
#     if color == "Gray":
#         gray.append(color)
#     elif color == 'Black':
#         black.append(color)
#     else:
#         cinnamon.append(color)
### With tools of pandas
gray = len(data[data["Primary Fur Color"] == "Gray"])
black = len(data[data["Primary Fur Color"] == "Black"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(f"Count of squirrels with gray color is - {gray}")
print(f"Count of squirrels with black color is - {black}")
print(f"Count of squirrels with cinnamon color is - {cinnamon}")
### construct dataFrames for converting into new csv-file
data_dict = {
    "Fur color": ['Gray', 'Cinnamon', 'Black'],
    "Count": [gray, black, cinnamon]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")