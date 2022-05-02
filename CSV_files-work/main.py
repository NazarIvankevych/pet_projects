<<<<<<< HEAD
### !TODO: Working with csv files in simple way with csv-module. Only if have a few information
# import csv
#
# with open("weather_data.csv", "r") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print ( f'Column names are {", ".join ( row )}' )
#             line_count += 1
#         else:
#             print ( f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.' )
#             line_count += 1
#     print ( f'Processed {line_count} lines.' )

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     # temp_numbers = csv.DictReader(data_file)
#     # for col_temp in temp_numbers:
#     #     temperature.append(int(col_temp['temp']))
#     # print(temperature)
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#     print(temperature)


###!TODO: IF we have a lot of info, we need to use Pandas module.

import pandas as pd

data = pd.read_csv("weather_data.csv")
# print(data)
# data_rows = data.from_records(data)
# data_html = data.to_html()
# print(data_rows)
# print(data_html)

#!TODO: Calculate the average temperature
all_temperature = data['temp'].to_list()
print(f"All temperature from csv file - {all_temperature}")
### Answer in simple with basic loop
# count_temp = 0
# for num in all_temperature:
#     count_temp += num
# print(f"The average is - {round(count_temp / len(all_temperature))}^C")
### Answer with using pandas method - .mean()
# average = data['temp'].mean()
# print(f"The average is - {int(average)}^C")
### !TODO: max average with day
# max_average = data['temp'].max()
# print(f"Max average - {max_average}")
# print(f"The day is - {data[data.temp == data.temp.max()]}. Have a max average of temperature.")
=======
### !TODO: Working with csv files in simple way with csv-module. Only if have a few information
# import csv
#
# with open("weather_data.csv", "r") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print ( f'Column names are {", ".join ( row )}' )
#             line_count += 1
#         else:
#             print ( f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.' )
#             line_count += 1
#     print ( f'Processed {line_count} lines.' )

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     # temp_numbers = csv.DictReader(data_file)
#     # for col_temp in temp_numbers:
#     #     temperature.append(int(col_temp['temp']))
#     # print(temperature)
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#     print(temperature)


###!TODO: IF we have a lot of info, we need to use Pandas module.

import pandas as pd

data = pd.read_csv("weather_data.csv")
# print(data)
# data_rows = data.from_records(data)
# data_html = data.to_html()
# print(data_rows)
# print(data_html)

#!TODO: Calculate the average temperature
all_temperature = data['temp'].to_list()
print(f"All temperature from csv file - {all_temperature}")
### Answer in simple with basic loop
# count_temp = 0
# for num in all_temperature:
#     count_temp += num
# print(f"The average is - {round(count_temp / len(all_temperature))}^C")
### Answer with using pandas method - .mean()
# average = data['temp'].mean()
# print(f"The average is - {int(average)}^C")
### !TODO: max average with day
# max_average = data['temp'].max()
# print(f"Max average - {max_average}")
# print(f"The day is - {data[data.temp == data.temp.max()]}. Have a max average of temperature.")
>>>>>>> 6bb0f90e7b2042da98278b61b14da243c44df510
