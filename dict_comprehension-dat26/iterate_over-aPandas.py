import pandas

student_dict = {
    "students": ['Beth',  'Freddie', 'Alex', 'Caroline', 'Dave', 'Eleanor'],
    "scores": [96, 92, 55, 35, 67, 60]
}
# for (key, value) in student_dict.items():
#     print(value)

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame, '\n\nWith a dataframe loop:')
# Loop throught rows of the a data frame
for (index, row) in student_data_frame.iterrows():
    # print(row)
    # If you get some particular row then we must use condition and call that row
    if row.students == 'Beth':
        print(f"Score of Angela - {row.scores}")